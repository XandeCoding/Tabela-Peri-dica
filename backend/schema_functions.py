"""Ferramentas de manuseio e Inicializaçao do Banco de dados."""
from tinymongo import TinyMongoClient
from schema import Elemento, Pesquisa


def init_Elementos() -> list:
    """Inicializa e instância a estrutura do banco de dados."""
    hidrogenio = Elemento('H', 'Hidrogênio', 'Metais Alcalinos', 1, 1.008)
    litio = Elemento('Li', 'Lítio', 'Metais Alcalinos', 3, 6.94)
    sodio = Elemento('Na', 'Sódio', 'Metais Alcalinos', 11, 22.990)
    potassio = Elemento('K', 'Potásio', 'Metais Alcalinos', 19, 39.098)
    rubidio = Elemento('Rb', 'Rubídio', 'Metais Alcalinos', 37, 85.468)
    cesio = Elemento('Cs', 'Césio', 'Metais Alcalinos', 55, 132.91)
    francio = Elemento('Fr', 'Frâncio', 'Metais Alcalinos', 87, 223)
    berilio = Elemento('Be', 'Berílio', 'Metais alcalinos Terrosos', 4, 9.0122)
    magnesio = Elemento(
        'Mg', 'Magnésio', 'Metais alcalinos Terrosos', 12, 24.305)
    calcio = Elemento('Ca', 'Cálcio', 'Metais alcalinos Terrosos', 20, 24.305)
    estroncio = Elemento(
        'Sr', 'Estrôncio', 'Metais alcalinos Terrosos', 38, 87.62)
    bario = Elemento('Ba', 'Bário', 'Metais alcalinos Terrosos', 56, 137.33)
    radio = Elemento('Ra', 'Rádio', 'Metais alcalinos Terrosos', 88, 226)
    escandio = Elemento('Sc', 'Escândio', 'Metais de Transição', 21, 44.956)
    itrio = Elemento('Y', 'Ítrio', 'Metais de Transição', 39, 88.906)
    titanio = Elemento('Ti', 'Titânio', 'Metais de Transição', 22, 47.867)
    zirconio = Elemento('Zr', 'Zircônio', 'Metais de Transição', 40, 91.224)
    hafnio = Elemento('Hf', 'Háfnio', 'Metais de Transição', 72, 178.49)
    rutherfordio = Elemento('Rf', 'Rutherfórdio',
                            'Metais de Transição', 104, 267)
    vanadio = Elemento('V', 'Vanádio', 'Metais de Transição', 23, 50.942)
    niobio = Elemento('Nb', 'Nióbio', 'Metais de Transição', 41, 92.906)
    tantalo = Elemento('Ta', 'Tântalo', 'Metais de Transição', 73, 180.95)
    dubnio = Elemento('Db', 'Dúbnio', 'Metais de Transição', 105, 268)
    cromio = Elemento('Cr', 'Crômio', 'Metais de Transição', 24, 51.996)
    molibdenio = Elemento('Mo', 'Molibdênio', 'Metais de Transição', 42, 95.95)
    tungstenio = Elemento('W', 'Tungstênio', 'Metais de Transição', 74, 183.84)
    seaborgio = Elemento('Sg', 'Seabórgio', 'Metais de Transição', 106, 269)
    manganes = Elemento('Mn', 'Manganês', 'Metais de Transição', 25, 54.938)
    tecnecio = Elemento('Tc', 'Tecnécio', 'Metais de Transição', 43, 98)
    renio = Elemento('Re', 'Rênio', 'Metais de Transição', 75, 186.21)
    bohrio = Elemento('Bh', 'Bóhrio', 'Metais de Transição', 107, 270)
    ferro = Elemento('Fe', 'Ferro', 'Metais de Transição', 26, 55.845)
    rutenio = Elemento('Ru', 'Rutênio', 'Metais de Transição', 44, 101.07)
    osmio = Elemento('Os', 'Ósmio', 'Metais de Transição', 76, 190.23)
    hassio = Elemento('Hs', 'Hássio', 'Metais de Transição', 108, 277)
    cobalto = Elemento('Co', 'Cobalto', 'Metais de Transição', 27, 58.933)
    rodio = Elemento('Rh', 'Ródio', 'Metais de Transição', 45, 102.91)
    iridio = Elemento('Ir', 'Irídio', 'Metais de Transição', 77, 192.22)
    meitnerio = Elemento('Mt', 'Meitnério', 'Metais de Transição', 109, 278)
    niquel = Elemento('Ni', 'Níquel', 'Metais de Transição', 28, 58.693)
    paladio = Elemento('Pd', 'Paládio', 'Metais de Transição', 46, 106.42)
    platina = Elemento('Pt', 'Platina', 'Metais de transição', 78, 195.08)
    darmstacio = Elemento('Ds', 'Darmstácio', 'Metais de Transição', 110, 281)
    cobre = Elemento('Cu', 'Cobre', 'Metais de Transição', 29, 63.546)
    prata = Elemento('Ag', 'Prata', 'Metais de Transição', 47, 107.87)
    ouro = Elemento('Au', 'Ouro', 'Metais de Transição', 79, 196.97)
    roentgenio = Elemento('Rg', 'Roentgênio', 'Metais de Transição', 111, 282)
    zinco = Elemento('Zn', 'Zinco', 'Metais de Transição', 30, 65.38)
    cadmio = Elemento('Cd', 'Cádmio', 'Metais de Transição', 48, 112.41)
    mercurio = Elemento('Hg', 'Mercúrio', 'Metais de Transição', 80, 200.59)
    copernicio = Elemento('Cn', 'Copernício', 'Metais de Transição', 112, 285)
    boro = Elemento('B', 'Boro', 'Semimetais', 5, 10.81)
    aluminio = Elemento(
        'Al', 'Alumínio', 'Metais de Pós Transiçao', 13, 26.982)
    galio = Elemento('Ga', 'Gálio', 'Metais de Pós Transiçao', 31, 69.723)
    indio = Elemento('In', 'Índio', 'Metais de Pós Transiçao', 49, 114.82)
    talio = Elemento('Tl', 'Tálio', 'Metais de Pós Transiçao', 81, 204.38)
    nihonium = Elemento('Nh', 'Nihonium', 'Desconhecida', 113, 286)
    carbono = Elemento('C', 'Carbono', 'Outros não metais', 6, 12.011)
    silicio = Elemento('Si', 'Silício', 'Semimetais', 14, 28.085)
    germanio = Elemento('Ge', 'Germânio', 'Semimetais', 32, 72.630)
    estanho = Elemento('Sn', 'Estanho', 'Metais de Pós Transiçao', 50, 118.71)
    chumbo = Elemento('Pb', 'Chumbo', 'Metais de Pós Transiçao', 82, 207.2)
    flerovio = Elemento('Fl', 'Fleróvio', 'Metais de Pós Transiçao', 114, 289)
    azoto = Elemento('N', 'Azoto', 'Outros não metais', 7, 14.007)
    fosforo = Elemento('P', 'Fosforo', 'Outros não metais', 15, 30.974)
    arsenio = Elemento('As', 'Arsênio', 'Semimetais', 33, 74.922)
    antimonio = Elemento('Sb', 'Antimônio', 'Semimetais', 51, 121.76)
    bismuto = Elemento('Bi', 'Bismuto', 'Metais de Pós Transiçao', 83, 208.98)
    moscovium = Elemento('Mc', 'Moscovium', 'Desconhecida', 115, 290)
    oxigenio = Elemento('O', 'Oxigênio', 'Outros não metais', 8, 15.999)
    enxofre = Elemento('S', 'Enxofre', 'Outros não metais', 16, 32.06)
    selenio = Elemento('Se', 'Selênio', 'Outros não metais', 34, 78.971)
    telurio = Elemento('Te', 'Telúrio', 'Semimetais', 52, 127.60)
    polonio = Elemento('Po', 'Polônio', 'Metais de Pós Transiçao', 84, 209)
    livermorio = Elemento('Lv', 'Livermório', 'Desconhecida', 116, 293)
    fluor = Elemento('F', 'Flúor', 'Outros não metais', 9, 18.998)
    cloro = Elemento('Cl', 'Cloro', 'Outros não metais', 17, 35.45)
    bromo = Elemento('Br', 'Bromo', 'Outros não metais', 35, 79.904)
    iodo = Elemento('I', 'Iodo', 'Outros não metais', 53, 126.90)
    astato = Elemento('At', 'Astato', 'Semimetais', 85, 210)
    tennessine = Elemento('Ts', 'Tennessine', 'Desconhecida', 117, 294)
    helio = Elemento('He', 'Hélio', 'Gases Nobres', 2, 4.0026)
    neon = Elemento('Ne', 'Néon', 'Gases Nobre', 10, 20.180)
    argon = Elemento('Ar', 'Argon', 'Gases Nobres', 18, 39.948)
    cripton = Elemento('Kr', 'Crípton', 'Gases Nobres', 36, 83.798)
    xenonio = Elemento('Xe', 'Crípton', 'Gases Nobres', 54, 131.29)
    radion = Elemento('Rn', 'Rádon', 'Gases Nobres', 86, 222)
    oganesson = Elemento('Og', 'Oganesson', 'Gases Nobres', 118, 294)
    lantanio = Elemento('La', 'Lantânio', 'Lantanóides', 57, 138.91)
    actinio = Elemento('Ac', 'Actínio', 'Actinóides', 89, 227)
    cerio = Elemento('Ce', 'Cério', 'Lantanóides', 58, 140.12)
    torio = Elemento('Th', 'Tório', 'Actinóides', 90, 232.04)
    praseodimio = Elemento('Pr', 'Prasiodímio', 'Actinóides', 59, 140.91)
    protactinio = Elemento('Pa', 'Proctactínio', 'Actinóides', 91, 231.04)
    neodimio = Elemento('Nd', 'Neodímio', 'Lantanóides', 60, 144.24)
    uranio = Elemento('U', 'Urânio', 'Actinóides', 92, 238.03)
    promecio = Elemento('Pm', 'Promécio', 'Lantanóides', 61, 145)
    neptunio = Elemento('Np', 'Neptúnio', 'Actinóides', 93, 237)
    samario = Elemento('Sm', 'Samário', 'Lantanóides', 62, 150.36)
    plutonio = Elemento('Pu', 'Plutônio', 'Actinóides', 94, 244)
    europio = Elemento('Eu', 'Európio', 'Lantanóides', 63, 151.96)
    americio = Elemento('Am', 'Amerício', 'Actinóides', 95, 243)
    gadolinio = Elemento('Gd', 'Gadolínio', 'Lantanóides', 64, 157.25)
    curio = Elemento('Cm', 'Cúrio', 'Actinóides', 96, 247)
    terbio = Elemento('Tb', 'Térbio', 'Lantanóides', 65, 158.93)
    berquelio = Elemento('Bk', 'Berquélio', 'Actinóides', 97, 247)
    disprosio = Elemento('Dy', 'Disprósio', 'Lantanóides', 66, 162.50)
    californio = Elemento('Cf', 'Califórnio', 'Actinóides', 98, 251)
    holmio = Elemento('Ho', 'Hólmio', 'Lantanóides', 67, 164)
    einstenio = Elemento('Es', 'Einstênio', 'Actinóides', 99, 252)
    erbio = Elemento('Er', 'Erbio', 'Lantanóides', 68, 167)
    fermio = Elemento('Fm', 'Férmio', 'Actinóides', 100, 257)
    tulio = Elemento('Tm', 'Túlio', 'Lantanóides', 69, 168.93)
    mendelevio = Elemento('Md', 'Mendelévio', 'Actinóides', 101, 258)
    iterbio = Elemento('Yb', 'Itérbio', 'Lantanóides', 70, 173.05)
    nobelio = Elemento('No', 'Nobélio', 'Actinóides', 102, 259)
    lutecio = Elemento('Lu', 'Lutécio', 'Lantanóides', 71, 174.97)
    laurencio = Elemento('Lr', 'Laurêncio', 'Actinóides', 103, 266)

    lista = (hidrogenio, litio, sodio, potassio, rubidio,
             cesio, francio, berilio, magnesio, calcio, estroncio,
             bario, radio, escandio, itrio, titanio, zirconio,
             hafnio, rutherfordio, vanadio, niobio, tantalo, dubnio,
             cromio, molibdenio, tungstenio, seaborgio, manganes,
             tecnecio, renio, bohrio, ferro, rutenio, osmio, hassio,
             cobalto, rodio, iridio, meitnerio, niquel, paladio,
             platina, darmstacio, cobre, prata, ouro, roentgenio,
             zinco, cadmio, mercurio, copernicio, boro, aluminio,
             galio, indio, talio, nihonium, carbono, silicio,
             germanio, estanho, chumbo, flerovio, azoto, fosforo,
             arsenio, antimonio, bismuto, moscovium, oxigenio,
             enxofre, selenio, telurio, polonio, livermorio,
             fluor, cloro, bromo, iodo, astato, tennessine, helio,
             neon, argon, cripton, xenonio, radion, oganesson,
             lantanio, actinio, cerio, torio, praseodimio, protactinio,
             neodimio, uranio, promecio, neptunio, samario, plutonio,
             europio, americio, gadolinio, curio, terbio, berquelio,
             disprosio, californio, holmio, einstenio, erbio, fermio,
             tulio, mendelevio, iterbio, nobelio, lutecio, laurencio)
    return lista


def init_Pesquisa(elementos: list) -> list:
    """Inicializa e instância a estrutura de pesquisa no banco de dados."""
    pesquisaLista = list()
    for elemento in elementos:
        pesquisaLista.append(Pesquisa(
                                      sigla=elemento.sigla,
                                      nome=elemento.nome,
                                      familia=elemento.familia)
                             )
    return pesquisaLista


def init_BancoDeDados_TinyMongo(elementos: list):
    """Adição dos elementos no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos

    for elemento in elementos:
        collection.insert_one({
                              'sigla': elemento.sigla,
                              'nome': elemento.nome,
                              'familia': elemento.familia,
                              'atomico': elemento.atomico,
                              'm_molar': elemento.m_molar
                              }
                              ).inserted_id


def init_System():
    """Inicializa a lista de pesquisa e o Banco de dados."""
    elementos = init_Elementos()
    pesquisa = init_Pesquisa(elementos)
    init_BancoDeDados_TinyMongo(elementos)
    return pesquisa


def jsonToElemento(json: dict) -> Elemento:
    """
    Trata o dado retornado pelo banco de dados.

    Transforma o retorno do banco de dados que é em json mas tratado em python
    como dict, para uma de instância Elemento.
    """
    elemento = Elemento(
                        json.get('sigla'),
                        json.get('nome'),
                        json.get('familia'),
                        json.get('atomico'),
                        json.get('m_molar')
                       )
    return elemento


def buscaElemento_Sigla(chave: str) -> Elemento:
    """Busca a sigla do elemento no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos
    info = collection.find_one({'sigla': chave})

    return info


def buscaElemento_Nome(chave: str) -> Elemento:
    """Busca o nome do elemento no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos
    info = collection.find_one({'nome': chave})

    return info


def buscaElemento_Familia(chave: str) -> Elemento:
    """Busca os elementos de determinada familia no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos
    info = collection.find({'familia': chave})

    return info
