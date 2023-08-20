    conn = Connection()
    #print(conn.connection)
    sql = '''INSERT INTO glb.produto (descricao, pesobruto, pesoliquido) VALUES ('teste', 10, 10);
          '''
    x = conn.insert(sql)
    print(x)
    
    tuplas = (('teste 1', 20, 20), ('teste 2', 21, 21),('teste 3', 23, 23),('teste 4', 24, 24),
             ('teste 5', 25, 25), ('teste 6', 26, 26), ('teste 7', 27, 27))
    sql = 'INSERT INTO glb.produto (descricao, pesobruto, pesoliquido) VALUES (%s, %s, %s)'
    
    x = conn.insertmany(sql, tuplas)
    
    q = 'SELECT * FROM glb.produto'
    curs = conn.select(q)
    for record in curs:
        print(record)
        
    sql = 'DELETE FROM glb.produto WHERE idproduto > 300'
    conn.delete(sql)
    conn.connection.close()
    
