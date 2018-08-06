class Elemento:
	"""Representacao de um elemento.
	attributes: nome, sigla, atomico, m_molar.
	"""
	def __init__(self, 
		sigla = 'none', nome = 'none', familia = 'none',
		 atomico = 0, m_molar = 0):
		self.sigla = sigla
		self.nome = nome
		self.familia = familia
		self.atomico = 0
		self.m_molar = 0.0
	def __str__ (self):
		return ("%s %s\nFamilia: %s\nNumero atomico: %d\nMassa Molar %.4f\n " % (self.sigla, self.nome, self.familia, self.atomico, self.m_molar))

# Inicializaçao da estrutura da tabela
def inicializa_estrutura ():	
	hidrogenio = Elemento()
	hidrogenio.sigla = 'H'
	hidrogenio.nome = 'Hidrogênio'
	hidrogenio.familia = 'Metais Alcalinos'
	hidrogenio.atomico = 1
	hidrogenio.m_molar = 1.008


	litio = Elemento()
	litio.sigla = 'Li'
	litio.nome = 'Lítio'
	litio.familia = 'Metais Alcalinos'
	litio.atomico = 3
	litio.m_molar = 6.94

	sodio = Elemento()
	sodio.sigla = 'Na'
	sodio.nome = 'Sódio'
	sodio.familia = 'Metais Alcalinos'
	sodio.atomico = 11
	sodio.m_molar = 22.990

	potassio = Elemento()
	sodio.sigla = 'K'
	sodio.nome = 'Potásio'
	sodio.familia = 'Metais Alcalinos'
	sodio.atomico = 19
	sodio.m_molar = 39.098

	rubidio = Elemento()
	rubidio.sigla = 'Rb'
	rubidio.nome = 'Rubídio'
	rubidio.familia = 'Metais Alcalinos'
	rubidio.atomico = 37
	rubidio.m_molar = 85.468

	cesio = Elemento()
	cesio.sigla = 'Cs'
	cesio.nome = 'Césio'
	cesio.familia = 'Metais Alcalinos'
	cesio.atomico = 55
	cesio.m_molar = 132.91

	francio = Elemento()
	francio.sigla = 'Fr'
	francio.nome = 'Frâncio'
	francio.familia = 'Metais Alcalinos'
	francio.atomico = 87
	francio.m_molar = 223

	berilio = Elemento()
	berilio.sigla = 'Be'
	berilio.nome = 'Berílio'
	berilio.familia = 'Metais alcalinos Terrosos'
	berilio.atomico = 4
	berilio.m_molar = 9.0122

	magnesio = Elemento()
	magnesio.sigla = 'Mg'
	magnesio.nome = 'Magnésio'
	magnesio.familia = 'Metais alcalinos Terrosos'
	magnesio.atomico = 12
	magnesio.m_molar = 24.305

	calcio = Elemento()
	calcio.sigla = 'Ca'
	calcio.nome = 'Cálcio'
	calcio.familia = 'Metais alcalinos Terrosos'
	calcio.atomico = 20
	calcio.m_molar = 24.305

	estroncio = Elemento()
	estroncio.sigla = 'Sr'
	estroncio.nome = 'Estrôncio'
	estroncio.familia = 'Metais alcalinos Terrosos'
	estroncio.atomico = 38
	estroncio.m_molar = 87.62

	bario = Elemento ()
	bario.sigla = 'Ba'
	bario.nome = 'Bário'
	bario.familia = 'Metais alcalinos Terrosos'
	bario.atomico = 56
	bario.m_molar = 137.33

	radio = Elemento()
	radio.sigla = 'Ra'
	radio.nome = 'Rádio'
	radio.familia = 'Metais alcalinos Terrosos'
	radio.atomico = 88
	radio.m_molar = 226

	escandio = Elemento()
	escandio.sigla = 'Sc'
	escandio.nome = 'Escândio'
	escandio.familia = 'Metais de Transição'
	escandio.atomico = 21
	escandio.m_molar = 44.956

	itrio = Elemento()
	itrio.sigla = 'Y'
	itrio.nome = 'Ítrio'
	itrio.familia = 'Metais de Transição'
	itrio.atomico = 39
	itrio.m_molar = 88.906

	titanio = Elemento()
	titanio.sigla = 'Ti'
	titanio.nome = 'Titânio'
	titanio.familia = 'Metais de Transição'
	titanio.atomico = 22
	titanio.m_molar = 47.867

	zirconio = Elemento()
	zirconio.sigla = 'Zr'
	zirconio.nome = 'Zircônio'
	zirconio.familia = 'Metais de Transição'
	zirconio.atomico = 40
	zirconio.m_molar = 91.224

	hafnio = Elemento()
	hafnio.sigla = 'Hf'
	hafnio.nome = 'Háfnio'
	hafnio.familia = 'Metais de Transição'
	hafnio.atomico = 72
	hafnio.m_molar = 178.49

	rutherfordio = Elemento()
	rutherfordio.sigla = 'Rf'
	rutherfordio.nome = 'Rutherfórdio'
	rutherfordio.familia = 'Metais de Transição'
	rutherfordio.atomico = 104
	rutherfordio.m_molar = 267

	vanadio = Elemento ()
	vanadio.sigla = 'V'
	vanadio.nome = 'Vanádio'
	vanadio.familia = 'Metais de Transição'
	vanadio.atomico = 23
	vanadio.m_molar = 50.942

	niobio = Elemento()
	niobio.sigla = 'Nb'
	niobio.nome = 'Nióbio'
	niobio.familia = 'Metais de Transição'
	niobio.atomico = 41
	niobio.m_molar = 92.906

	tantalo = Elemento()
	tantalo.sigla = 'Ta'
	tantalo.nome = 'Tântalo'
	tantalo.familia = 'Metais de Transição'
	tantalo.atomico = 73
	tantalo.m_molar = 180.95

	dubnio = Elemento()
	dubnio.sigla = 'Db'
	dubnio.nome = 'Dúbnio'
	dubnio.familia = 'Metais de Transição'
	dubnio.atomico = 105
	dubnio.m_molar = 268

	cromio = Elemento()
	cromio.sigla = 'Cr'
	cromio.nome = 'Crômio'
	cromio.familia = 'Metais de Transição'
	cromio.atomico = 24
	cromio.m_molar = 51.996

	molibdenio = Elemento()
	molibdenio.sigla = 'Mo'
	molibdenio.nome = 'Molibdênio'
	molibdenio.familia = 'Metais de Transição'
	molibdenio.atomico = 42
	molibdenio.m_molar = 95.95

	tungstenio = Elemento()
	tungstenio.sigla = 'W'
	tungstenio.nome = 'Tungstênio'
	tungstenio.familia = 'Metais de Transição'
	tungstenio.atomico = 74
	tungstenio.m_molar = 183.84

	seaborgio = Elemento()
	seaborgio.sigla = 'Sg'
	seaborgio.nome = 'Seabórgio'
	seaborgio.familia = 'Metais de Transição'
	seaborgio.atomico = 106
	seaborgio.m_molar = 269

	manganes = Elemento()
	manganes.sigla = 'Mn'
	manganes.nome = 'Manganês'
	manganes.familia = 'Metais de Transição'
	manganes.atomico = 25
	manganes.m_molar = 54.938

	tecnecio = Elemento()
	tecnecio.sigla = 'Tc'
	tecnecio.nome = 'Tecnécio'
	tecnecio.familia = 'Metais de Transição'
	tecnecio.atomico = 43
	tecnecio.m_molar = 98

	renio = Elemento()
	renio.sigla	= 'Re'
	renio.nome = 'Rênio'
	renio.familia = 'Metais de Transição'
	renio.atomico = 75
	renio.m_molar = 186.21

	bohrio = Elemento()
	bohrio.sigla = 'Bh'
	bohrio.nome = 'Bóhrio'
	bohrio.familia = 'Metais de Transição'
	bohrio.atomico = 107
	bohrio.m_molar = 270

	ferro = Elemento()
	ferro.sigla = 'Fe'
	ferro.nome = 'Ferro'
	ferro.familia = 'Metais de Transição'
	ferro.atomico = 26
	ferro.m_molar = 55.845

	rutenio = Elemento()
	rutenio.sigla = 'Ru'
	rutenio.nome = 'Rutênio'
	rutenio.familia = 'Metais de Transição'
	rutenio.atomico = 44
	rutenio.m_molar = 101.07

	osmio = Elemento()
	osmio.sigla = 'Os'
	osmio.nome = 'Ósmio'
	osmio.familia = 'Metais de Transição'
	osmio.atomico = 76
	osmio.m_molar = 190.23

	hassio = Elemento()
	hassio.sigla = 'Hs'
	hassio.nome = 'Hássio'
	hassio.familia = 'Metais de Transição'
	hassio.atomico = 108
	hassio.m_molar = 277

	cobalto = Elemento()
	cobalto.sigla = 'Co'
	cobalto.nome = 'Cobalto'
	cobalto.familia = 'Metais de Transição'
	cobalto.atomico = 27
	cobalto.m_molar = 58.933

	rodio = Elemento()
	rodio.sigla = 'Rh'
	rodio.nome = 'Ródio'
	rodio.familia = 'Metais de Transição'
	rodio.atomico = 45
	rodio.m_molar = 102.91

	iridio = Elemento()
	iridio.sigla = 'Ir'
	iridio.nome = 'Irídio'
	iridio.familia = 'Metais de Transição'
	iridio.atomico = 77
	iridio.m_molar = 192.22

	meitnerio = Elemento()
	meitnerio.sigla = 'Mt'
	meitnerio.nome = 'Meitnério'
	meitnerio.familia = 'Metais de Transição'
	meitnerio.atomico = 109
	meitnerio.m_molar = 278

	niquel = Elemento()
	niquel.sigla = 'Ni'
	niquel.nome = 'Níquel'
	niquel.familia = 'Metais de Transição'
	niquel.atomico = 28
	niquel.m_molar = 58.693

	paladio = Elemento()
	paladio.sigla = 'Pd'
	paladio.nome = 'Paládio'
	paladio.familia = 'Metais de Transição'
	paladio.atomico = 46
	paladio.m_molar = 106.42

	platina = Elemento()
	platina.sigla = 'Pt'
	platina.nome = 'Platina'
	platina.familia = 'Metais de transição'
	platina.atomico = 78
	platina.m_molar = 195.08

	darmstacio = Elemento()
	darmstacio.sigla = 'Ds'
	darmstacio.nome = 'Darmstácio'
	darmstacio.familia = 'Metais de Transição'
	darmstacio.atomico = 110
	darmstacio.m_molar = 281

	cobre = Elemento()
	cobre.sigla = 'Cu'
	cobre.nome = 'Cobre'
	cobre.familia = 'Metais de Transição'
	cobre.atomico = 29
	cobre.m_molar = 63.546

	prata = Elemento()
	prata.sigla = 'Ag'
	prata.nome = 'Prata'
	prata.familia = 'Metais de Transição'
	prata.atomico = 47
	prata.m_molar = 107.87

	ouro = Elemento()
	ouro.sigla = 'Au'
	ouro.nome = 'Ouro'
	ouro.familia = 'Metais de Transição'
	ouro.atomico = 79
	ouro.m_molar = 196.97

	roentgenio = Elemento()
	roentgenio.sigla = 'Rg'
	roentgenio.nome = 'Roentgênio'
	roentgenio.familia = 'Metais de Transição'
	roentgenio.atomico = 111
	roentgenio.m_molar = 282

	zinco = Elemento()
	zinco.sigla	= 'Zn'
	zinco.nome = 'Zinco'
	zinco.familia = 'Metais de Transição'
	zinco.atomico = 30
	zinco.m_molar = 65.38

	cadmio = Elemento()
	cadmio.sigla = 'Cd'
	cadmio.nome = 'Cádmio'
	cadmio.familia = 'Metais de Transição'
	cadmio.atomico = 48
	cadmio.m_molar = 112.41

	mercurio = Elemento()
	mercurio.sigla = 'Hg'
	mercurio.nome = 'Mercúrio'
	mercurio.familia = 'Metais de Transição'
	mercurio.atomico = 80
	mercurio.m_molar = 200.59

	copernicio = Elemento()
	copernicio.sigla = 'Cn'
	copernicio.nome = 'Copernício'
	copernicio.familia = 'Metais de Transição'
	copernicio.atomico = 112
	copernicio.m_molar = 285

	boro = Elemento()
	boro.sigla = 'B'
	boro.nome = 'Boro'
	boro.familia = 'Semimetais'
	boro.atomico = 5
	boro.m_molar = 10.81

	aluminio = Elemento()
	aluminio.sigla = 'Al'
	aluminio.nome = 'Alumínio'
	aluminio.familia = 'Metais de Pós Transiçao'
	aluminio.atomico = 13
	aluminio.m_molar = 26.982

	galio = Elemento()
	galio.sigla = 'Ga'
	galio.nome = 'Gálio'
	galio.familia = 'Metais de Pós Transiçao'
	galio.atomico = 31
	galio.m_molar = 69.723

	indio = Elemento()
	indio.sigla = 'In'
	indio.nome = 'Índio'
	indio.familia = 'Metais de Pós Transiçao'
	indio.atomico = 49
	indio.m_molar = 114.82

	talio = Elemento()
	talio.sigla = 'Tl'
	talio.nome = 'Tálio'
	talio.familia = 'Metais de Pós Transiçao'
	talio.atomico = 81
	talio.m_molar = 204.38

	nihonium = Elemento()
	nihonium.sigla = 'Nh'
	nihonium.nome = 'Nihonium'
	nihonium.familia = 'Desconhecida'
	nihonium.atomico = 113
	nihonium.m_molar = 286

	carbono = Elemento()
	carbono.sigla = 'C'
	carbono.nome = 'Carbono'
	carbono.familia = 'Outros não metais'
	carbono.atomico = 6
	carbono.m_molar = 12.011

	silicio = Elemento()
	silicio.sigla = 'Si'
	silicio.nome = 'Silício'
	silicio.familia = 'Semimetais'
	silicio.atomico	= 14
	silicio.m_molar = 28.085

	germanio = Elemento()
	germanio.sigla = 'Ge'
	germanio.nome = 'Germânio'
	germanio.familia = 'Semimetais'
	germanio.atomico = 32
	germanio.m_molar = 72.630

	estanho = Elemento()
	estanho.sigla = 'Sn'
	estanho.nome = 'Estanho'
	estanho.familia = 'Metais de Pós Transiçao'
	estanho.atomico = 50
	estanho.m_molar = 118.71

	chumbo = Elemento()
	chumbo.sigla = 'Pb'
	chumbo.nome = 'Chumbo'
	chumbo.familia = 'Metais de Pós Transiçao'
	chumbo.atomico = 82
	chumbo.m_molar = 207.2

	flerovio = Elemento()
	flerovio.sigla = 'Fl'
	flerovio.nome = 'Fleróvio'
	flerovio.familia = 'Metais de Pós Transiçao'
	flerovio.atomico = 114
	flerovio.m_molar = 289

	azoto = Elemento()
	azoto.sigla = 'N'
	azoto.nome = 'Azoto'
	azoto.familia = 'Outros não metais'
	azoto.atomico = 7
	azoto.m_molar = 14.007

	fosforo = Elemento()
	fosforo.sigla = 'P'
	fosforo.nome = 'Fosforo'
	fosforo.familia = 'Outros não metais'
	fosforo.atomico = 15
	fosforo.m_molar = 30.974

	arsenio = Elemento()
	arsenio.sigla = 'As'
	arsenio.nome = 'Arsênio'
	arsenio.familia = 'Semimetais'
	arsenio.atomico = 33
	arsenio.m_molar = 74.922

	antimonio = Elemento()
	antimonio.sigla = 'Sb'
	antimonio.nome ='Antimônio'
	antimonio.familia = 'Semimetais'
	antimonio.atomico = 51
	antimonio.m_molar = 121.76

	bismuto = Elemento()
	bismuto.sigla = 'Bi'
	bismuto.nome = 'Bismuto'
	bismuto.familia = 'Metais de Pós Transiçao'
	bismuto.atomico = 83
	bismuto.m_molar = 208.98

	moscovium = Elemento()
	moscovium.sigla = 'Mc'
	moscovium.nome = 'Moscovium'
	moscovium.familia = 'Desconhecida'
	moscovium.atomico = 115
	moscovium.m_molar = 290

	oxigenio = Elemento()
	oxigenio.sigla = 'O'
	oxigenio.nome = 'Oxigênio'
	oxigenio.familia = 'Outros não metais'
	oxigenio.atomico = 8
	oxigenio.m_molar = 15.999

	enxofre = Elemento()
	enxofre.sigla = 'S'
	enxofre.nome = 'Enxofre'
	enxofre.familia = 'Outros não metais'
	enxofre.atomico = 16
	enxofre.m_molar = 32.06

	selenio = Elemento()
	selenio.sigla = 'Se'
	selenio.nome = 'Selênio'
	selenio.familia = 'Outros não metais'
	selenio.atomico = 34
	selenio.m_molar = 78.971

	telurio = Elemento()
	telurio.sigla = 'Te'
	telurio.nome = 'Telúrio'
	telurio.familia = 'Semimetais'
	telurio.atomico = 52
	telurio.m_molar = 127.60

	polonio = Elemento()
	polonio.sigla = 'Po'
	polonio.nome = 'Polônio'
	polonio.familia = 'Metais de Pós Transiçao'
	polonio.atomico = 84
	polonio.m_molar = 209

	livermorio = Elemento()
	livermorio.sigla = 'Lv'
	livermorio.nome = 'Livermório'
	livermorio.familia = 'Desconhecida'
	livermorio.atomico = 116
	livermorio.m_molar = 293

	fluor = Elemento()
	fluor.sigla = 'F'
	fluor.nome = 'Flúor'
	fluor.familia = 'Outros não metais'
	fluor.atomico = 9
	fluor.m_molar = 18.998

	cloro = Elemento()
	cloro.sigla = 'Cl'
	cloro.nome = 'Cloro'
	cloro.familia = 'Outros não metais'
	cloro.atomico = 17
	cloro.m_molar = 35.45

	bromo = Elemento()
	bromo.sigla = 'Cl'
	bromo.nome = 'Bromo'
	bromo.familia ='Outros não metais'
	bromo.atomico = 35
	bromo.m_molar = 79.904

	iodo = Elemento()
	iodo.sigla = 'I'
	iodo.nome = 'Iodo'
	iodo.familia = 'Outros não metais'
	iodo.atomico = 53
	iodo.m_molar = 126.90

	astato = Elemento()
	astato.sigla = 'At'
	astato.nome = 'Astato'
	astato.familia = 'Semimetais'
	astato.atomico = 85
	astato.m_molar = 210

	tennessine = Elemento()
	tennessine.sigla = 'Ts'
	tennessine.nome = 'Tennessine'
	tennessine.familia = 'Desconhecida'
	tennessine.atomico = 117
	tennessine.m_molar = 294

	helio = Elemento()
	helio.sigla = 'He'
	helio.nome = 'Hélio'
	helio.familia = 'Gases Nobres'
	helio.atomico = 2
	helio.m_molar = 4.0026

	neon = Elemento()
	neon.sigla = 'Ne'
	neon.nome = 'Néon'
	neon.familia = 'Gases Nobre'
	neon.atomico = 10
	neon.m_molar = 20.180

	argon = Elemento()
	argon.sigla = 'Ar'
	argon.nome = 'Argon'
	argon.familia = 'Gases Nobres'
	argon.atomico = 18
	argon.m_molar = 39.948

	cripton = Elemento()
	cripton.sigla = 'Kr'
	cripton.nome = 'Crípton'
	cripton.familia = 'Gases Nobres'
	cripton.atomico = 36
	cripton.m_molar = 83.798

	xenonio =  Elemento()
	xenonio.sigla = 'Xe'
	xenonio.nome = 'Crípton'
	xenonio.familia = 'Gases Nobres'
	xenonio.atomico = 54
	xenonio.m_molar = 131.29

	radion = Elemento()
	radion.sigla = 'Rn'
	radion.nome = 'Rádon'
	radion.familia = 'Gases Nobres'
	radion.atomico = 86
	radion.m_molar = 222

	oganesson = Elemento()
	oganesson.sigla = 'Og'
	oganesson.nome = 'Oganesson'
	oganesson.familia = 'Gases Nobres'
	oganesson.atomico = 118
	oganesson.m_molar = 294


	lantanio = Elemento()
	lantanio.sigla = 'La'
	lantanio.nome = 'Lantânio'
	lantanio.familia = 'Lantanóides'
	lantanio.atomico = 57
	lantanio.m_molar = 138.91

	actinio = Elemento()
	actinio.sigla = 'Ac'
	actinio.nome = 'Actínio'
	actinio.familia = 'Actinóides'
	actinio.atomico = 89
	actinio.m_molar = 227

	cerio = Elemento()
	cerio.sigla = 'Ce'
	cerio.nome = 'Cério'
	cerio.familia = 'Lantanóides'
	cerio.atomico = 58
	cerio.m_molar = 140.12

	torio = Elemento()
	torio.sigla = 'Th'
	torio.nome = 'Tório'
	torio.familia = 'Actinóides'
	torio.atomico = 90
	torio.m_molar = 232.04

	praseodimio = Elemento()
	praseodimio.sigla = 'Pr'
	praseodimio.nome = 'Prasiodímio'
	praseodimio.familia = 'Actinóides'
	praseodimio.atomico = 59
	praseodimio.m_molar = 140.91

	protactinio = Elemento()
	protactinio.sigla = 'Pa'
	protactinio.nome = 'Proctactínio'
	protactinio.familia = 'Actinóides'
	protactinio.atomico = 91
	protactinio.m_molar = 231.04

	neodimio = Elemento()
	neodimio.sigla = 'Nd'
	neodimio.nome = 'Neodímio'
	neodimio.familia = 'Lantanóides'
	neodimio.atomico = 60
	neodimio.m_molar = 144.24

	uranio = Elemento()
	uranio.sigla = 'U'
	uranio.nome = 'Urânio'
	uranio.familia = 'Actinóides'
	uranio.atomico = 92
	uranio.m_molar = 238.03

	promecio = Elemento()
	promecio.sigla = 'Pm'
	promecio.nome = 'Promécio'
	promecio.familia = 'Lantanóides'
	promecio.atomico = 61
	promecio.m_molar = 145

	neptunio = Elemento()
	neptunio.sigla = 'Np'
	neptunio.nome = 'Neptúnio'
	neptunio.familia = 'Actinóides'
	neptunio.atomico = 93
	neptunio.m_molar = 237

	samario = Elemento()
	samario.sigla = 'Sm'
	samario.nome = 'Samário'
	samario.familia = 'Lantanóides'
	samario.atomico = 62
	samario.m_molar = 150.36

	plutonio = Elemento()
	plutonio.sigla = 'Pu'
	plutonio.nome = 'Plutônio'
	plutonio.familia = 'Actinóides'
	plutonio.atomico = 94
	plutonio.m_molar = 244

	europio = Elemento()
	europio.sigla = 'Eu'
	europio.nome = 'Európio'
	europio.familia = 'Lantanóides'
	europio.atomico = 63
	europio.m_molar = 151.96

	americio = Elemento()
	americio.sigla = 'Am'
	americio.nome = 'Amerício'
	americio.familia = 'Actinóides'
	americio.atomico = 95
	americio.m_molar = 243

	gadolinio = Elemento()
	gadolinio.sigla = 'Gd'
	gadolinio.nome = 'Gadolínio'
	gadolinio.familia = 'Lantanóides'
	gadolinio.atomico = 64
	gadolinio.m_molar = 157.25

	curio = Elemento()
	curio.sigla = 'Cm'
	curio.nome = 'Cúrio'
	curio.familia = 'Actinóides'
	curio.atomico = 96
	curio.m_molar = 247

	terbio = Elemento()
	terbio.sigla = 'Tb'
	terbio.nome = 'Térbio'
	terbio.familia = 'Lantanóides'
	terbio.atomico = 65
	terbio.m_molar = 158.93

	berquelio = Elemento()
	berquelio.sigla = 'Bk'
	berquelio.nome = 'Berquélio'
	berquelio.familia = 'Actinóides'
	berquelio.atomico = 97
	berquelio.m_molar = 247

	disprosio = Elemento()
	disprosio.sigla = 'Dy'
	disprosio.nome = 'Disprósio'
	disprosio.familia = 'Lantanóides'
	disprosio.atomico = 66
	disprosio.m_molar = 162.50

	californio = Elemento()
	californio.sigla = 'Cf'
	californio.nome = 'Califórnio'
	californio.familia = 'Actinóides'
	californio.atomico = 98
	californio.m_molar = 251

	holmio = Elemento()
	holmio.sigla = 'Ho'
	holmio.nome = 'Hólmio'
	holmio.familia = 'Lantanóides'
	holmio.atomico = 67
	holmio.m_molar = 164

	einstenio = Elemento()
	einstenio.sigla = 'Es'
	einstenio.nome = 'Einstênio'
	einstenio.familia = 'Actinóides'
	einstenio.atomico = 99
	einstenio.m_molar = 252

	erbio = Elemento()
	erbio.sigla = 'Er'
	erbio.nome = 'Erbio'
	erbio.familia = 'Lantanóides'
	erbio.atomico = 68
	erbio.m_molar = 167

	fermio = Elemento()
	fermio.sigla = 'Fm'
	fermio.nome = 'Férmio'
	fermio.familia = 'Actinóides'
	fermio.atomico = 100
	fermio.m_molar = 257

	tulio = Elemento()
	tulio.sigla = 'Tm'
	tulio.nome = 'Túlio'
	tulio.familia = 'Lantanóides'
	tulio.atomico = 69
	tulio.m_molar = 168.93

	mendelevio = Elemento()
	mendelevio.sigla = 'Md'
	mendelevio.nome = 'Mendelévio'
	mendelevio.familia = 'Actinóides'
	mendelevio.atomico = 101
	mendelevio.m_molar = 258

	iterbio = Elemento()
	iterbio.sigla = 'Yb'
	iterbio.nome = 'Itérbio'
	iterbio.familia = 'Lantanóides'
	iterbio.atomico = 70
	iterbio.m_molar = 173.05

	nobelio = Elemento()
	nobelio.sigla = 'No'
	nobelio.nome = 'Nobélio'
	nobelio.familia = 'Actinóides'
	nobelio.atomico = 102
	nobelio.m_molar = 259

	lutecio = Elemento()
	lutecio.sigla = 'Lu'
	lutecio.nome = 'Lutécio'
	lutecio.familia = 'Lantanóides'
	lutecio.atomico = 71
	lutecio.m_molar = 174.97

	laurencio = Elemento()
	laurencio.sigla = 'Lr'
	laurencio.nome = 'Laurêncio'
	laurencio.familia = 'Actinóides'
	laurencio.atomico = 103
	laurencio.m_molar = 266

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
def find_sigla (chave):
	count_1 = 0
	count_2 = 0
	tamanho = len(chave)
	print("Tamanho da chave %d" % tamanho)
	for count_1 in range(118):
		similaridade = 0		
		if len(list_elements[count_1].sigla) != tamanho:
			continue		
		# print (list_elements[count_1].sigla)
		for count_2 in range(tamanho):			
			if list_elements[count_1].sigla[count_2] == chave[count_2]:
				similaridade+=1
				if similaridade == tamanho:
					print ("Similiraridade %d" % similaridade)				
					return count_1
	return -1

def find_nome (chave):
	count_1 = 0
	count_2 = 0
	# Provavel armazena primeiro se 
	# a similaridade e valida, posicao e a similaridade
	provavel = [0, 0, 0]
	tamanho = len(chave)	
	print("Tamanho da chave %d" % tamanho)
	for count_1 in range(118):
		similaridade = 0
		percorrer = len(list_elements[count_1].nome)
		if (percorrer != tamanho 
			and percorrer > tamanho):
			continue
			
		for count_2 in range(percorrer):
			if list_elements[count_1].nome[count_2] == chave[count_2]:
				similaridade+=1
				if (similaridade > provavel[2]):
					provavel[1] = count_1
					provavel[2] = similaridade
				if (similaridade == tamanho):
					provavel[0] = 1
					return provavel
	if provavel[2] >= (tamanho/2):
		provavel[0] = 2

	return (provavel)

def busca ():	
	aux = pesquisa.get()
	# Coloca a primeira letra da string como maiuscula
	if (aux[0] >= "a"):
		pesquisado = (aux[0:1].upper()) + aux[1:] 
		del (aux)
	else :
		pesquisado = aux
		del (aux)
	print("Palavra a ser pesquisada %s" % pesquisado)
	if type (pesquisado) == str:
		tamanho = len(pesquisado)
		count = 0
		if (tamanho <= 2):
			result_find = find_sigla (pesquisado)
			print ("Posicao na estrutura %d" % result_find)
			if (result_find != -1):
				resposta.set(list_elements[result_find])
				return

		else:
			result_find = find_nome (pesquisado)
			print (result_find)
			if (result_find[0] != 0):
				resposta.set(list_elements[result_find[1]])
				return

		resposta.set ("Por favor digite a sigla ou\n o nome do elemento novamente")
		return
			
	
# Processamento principal
# Inicializaçao da estrutura dos dados e da interface
from tkinter import *

app = Tk()
app.title ('Tabela de Elementos')
Label(app, text = "Digite um elemento a ser procurado").pack()
pesquisa = Entry(app)
pesquisa.pack()
Button(app, text = "buscar", command = busca).pack()
resposta = StringVar()
resposta.set("Pesquisando")
resultado = Label(app, textvariable = resposta).pack()

list_elements = inicializa_estrutura()
#print ("%s" % (list_elements[0]))
app.mainloop()