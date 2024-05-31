
usuarios = {}
usuarios['pepe'] = {'algoritmo': '6', 'salt': 'GvPtNlFyIslskD5x', 'password': 'TLb1S7FbFR7G9.Q5dfzYR.GbCv99fa9dErsDXhc0mIDxmKRGUW6N.oHUrlHN55CfNXdJdP25iCxkCMnNqaZLh1'}
usuarios['limitado'] = {'algoritmo': '6', 'salt': 'wLn3hfSJdxalxrpH', 'password': 'PZbtfKfDbOU07UTorvtrao4.Rvlpj1lbKFOV6wiRISPmTWptpse9SdZU/d5jd9QYSxpR41z1cqbp2x9Z.IPa3/'}
usuarios['root'] = {'algoritmo': '6', 'salt': '832zdzhYIe6s/RLz', 'password': 'dKpEljRzW0ndjwzF.ftrFqSiuJP1UlWHPN4fGwt8xCEX.AVeYKZL11fEHbFo7eYWw5qGpDuaubE8NX5TQD/nQ.'}

numdelineas = int(input())
elegido = input()
eleccion = input()

if elegido == 'pepe':
    if eleccion == 'algoritmo':
        print(usuarios['pepe']['algoritmo'])
    if eleccion == 'salt':
        print(usuarios['pepe']['salt'])
    if eleccion == 'password':
        print(usuarios['pepe']['password'])

if elegido == 'limitado':
    if eleccion == 'algoritmo':
        print(usuarios['limitado']['algoritmo'])
    if eleccion == 'salt':
        print(usuarios['limitado']['salt'])
    if eleccion == 'password':
        print(usuarios['limitado']['password'])

if elegido == 'root':
    if eleccion == 'algoritmo':
        print(usuarios['root']['algoritmo'])
    if eleccion == 'salt':
        print(usuarios['root']['salt'])
    if eleccion == 'password':
        print(usuarios['root']['password'])