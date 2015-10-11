import pymssql

__author__ = 'Alex Libório Caranha'


def get_arguments_in_stored_procedure(stored_procedure, host, database):
    connection = pymssql.connect(host=host, database=database, as_dict=True)
    cursor = connection.cursor()

    result = list()

    cursor.execute("SP_HELP {0}".format(stored_procedure))

    cursor.nextset()
    for row in cursor:
        result.append((row['Parameter_name'], row['Type'], row['Length']))

    connection.close()
    return result


def get_databases_names(host):
    result = list()
    connection = pymssql.connect(host=host, as_dict=True)
    cursor = connection.cursor()

    cursor.execute("EXEC sp_databases")
    for row in cursor:
        phrase = "{0}".format(row['DATABASE_NAME'])
        result.append(phrase)

    sorted(result, key=lambda item: item[0])   # sort by age

    return result


def get_help_text_stored_procedure(stored_procedure, host, database):
    connection = pymssql.connect(host=host, database=database, as_dict=True)
    cursor = connection.cursor()

    result = ""

    cursor.execute("SP_HELPTEXT {0}".format(stored_procedure))

    for row in cursor:
        result = result + row['Text']

    connection.close()
    return result


#----------------------------------------
#Teste1
#cur.execute('SELECT * FROM USUARIO')

#for row in cur:
#    #print(row)
#    print("ID=[%d, %s], Name=[%s, %s]:" % (row['UsuarioID'], type(row['UsuarioID']), row['Login'], type(row['Login'])))
#----------------------------------------
#Teste2
#cur.execute('SP_HELPTEXT up_GetUsuario')
#for row in cur:
#    print(row)
#----------------------------------------
#Teste3: Listar todas as tabelas.
#cur.execute("SELECT * FROM sysobjects WHERE xtype='U'")
#for row in cur:
#    print(row['name'])
#----------------------------------------
#Teste4: Encontrar todas as stored procedures.
#SELECT name FROM sys.objects WHERE type = 'P' If you want to find it within a period then;
#SELECT name FROM sys.objects WHERE type = 'P' AND DATEDIFF(D,create_date, GETDATE()) <5

#cur.execute("SELECT name FROM sys.objects WHERE type = 'P'")
#for row in cur:
#    print(row['name'])
#----------------------------------------