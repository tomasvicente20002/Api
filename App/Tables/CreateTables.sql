-- Object:  Table [Aeroporto]

CREATE TABLE IF NOT EXISTS [Aeroporto](
	[ID_Aeroporto] INTEGER,
	[Nome_Aeroporto] TEXT,
	[ID_Local] TEXT,
	[Local_Aeroporto] TEXT
);

-- Object:  Table [Aviao]

CREATE TABLE IF NOT EXISTS [Aviao](
	[ID_Aviao] INTEGER,
	[Nome_Aviao] TEXT,
	[Tipo_Aviao] INTEGER
);

-- Object:  Table [Chegada]

CREATE TABLE IF NOT EXISTS [Chegada](
	[ID_Chegada] INTEGER,
	[Data_Hora_Chegada] TEXT,
	[ID_Aeroporto] INTEGER
);

-- Object:  Table [Classe_Voo]

CREATE TABLE IF NOT EXISTS [Classe_Voo](
	[ID_Classe] INTEGER,
	[Nome_Classe] TEXT,
	[Preco] [float] NULL,
	[Lotacao] INTEGER
);

-- Object:  Table [Empregado]

CREATE TABLE IF NOT EXISTS [Empregado](
	[ID_Empregado] INTEGER,
	[Nome_Empregado] TEXT,
	[Morada_Empregado] TEXT,
	[Telefone_Empregado] INTEGER,
	[Salario_Empregado] INTEGER,
	[Funcao_Empregado] TEXT
);

-- Object:  Table [Local]

CREATE TABLE IF NOT EXISTS [Local](
	[ID_Local] INTEGER,
	[Local] TEXT,
	[img] [image] NULL
);

-- Object:  Table [Mensagens]

CREATE TABLE IF NOT EXISTS [Mensagens](
	[Id_mensagem] INTEGER,
	[Nome] TEXT,
	[email] TEXT,
	[assunto] TEXT,
	[Conteudo] [text] NULL,
	[Respondido] [bit] NULL
);

-- Object:  Table [Partida]

CREATE TABLE IF NOT EXISTS [Partida](
	[ID_Partida] INTEGER,
	[Data_Hora_Partida] TEXT,
	[ID_Aeroporto] INTEGER,
	[Hora_Data_Partida] TEXT,
	[Local_Aeroporto] TEXT
);

-- Object:  Table [Passageiro]

CREATE TABLE IF NOT EXISTS [Passageiro](
	[ID_Passageiro] INTEGER,
	[Nome_Passageiro] TEXT,
	[Morada_Passageiro] TEXT,
	[Telefone_Passageiro] TEXT,
	[Email] TEXT,
	[Codi_postal] TEXT
);

-- Object:  Table [Piloto]

CREATE TABLE IF NOT EXISTS [Piloto](
	[ID_Piloto] INTEGER,
	[Nome_Piloto] TEXT,
	[Morada_Piloto] TEXT,
	[Telefone_Piloto] INTEGER,
	[Salario_Piloto] NUMERIC NULL,
	[NumeroH_Piloto] INTEGER,
	[Licenca_Piloto] INTEGER
);

-- Object:  Table [Piloto_TipoAviao]

CREATE TABLE IF NOT EXISTS [Piloto_TipoAviao](
	[ID_Piloto] INTEGER
	[ID_Tipo_Aviao] INTEGER NOT NULL
);

-- Object:  Table [Reserva]

CREATE TABLE IF NOT EXISTS [Reserva](
	[ID_Reserva] INTEGER,
	[Lugar_Reserva] INTEGER,
	[ID_Passageiro] INTEGER
	[ID_Classe] INTEGER,
	[Pa] [bit] NULL
);

-- Object:  Table [Tipo_Aviao]

CREATE TABLE IF NOT EXISTS [Tipo_Aviao](
	[Tipo_Aviao] INTEGER,
	[Fabricante_Aviao] TEXT,
	[Modelo_Aviao] TEXT
);

-- Object:  Table [Voo]

CREATE TABLE IF NOT EXISTS [Voo](
	[ID_Voo] INTEGER,
	[Partida_Voo] INTEGER,
	[Chegada_Voo] INTEGER,
	[ID_Aviao] INTEGER NOT NULL
);

-- Object:  Table [Voo_Aeroporto]

CREATE TABLE IF NOT EXISTS [Voo_Aeroporto](
	[ID_Voo] INTEGER
	[ID_Aeroporto] INTEGER NOT NULL
);

-- Object:  Table [Voo_Aviao]

CREATE TABLE IF NOT EXISTS [Voo_Aviao](
	[ID_Voo] INTEGER
	[ID_Aviao] INTEGER NOT NULL
);

-- Object:  Table [Voo_Classe]

CREATE TABLE IF NOT EXISTS [Voo_Classe](
	[ID_Voo] INTEGER
	[ID_Classe] INTEGER NOT NULL
);

-- Object:  Table [Voo_Empregado]

CREATE TABLE IF NOT EXISTS [Voo_Empregado](
	[ID_Voo] INTEGER
	[ID_Empregado] INTEGER
	[Funcao] TEXT
);

-- Object:  Table [Voo_Piloto]

CREATE TABLE IF NOT EXISTS [Voo_Piloto](
	[ID_Voo] INTEGER
	[ID_Piloto] INTEGER
);

-- Object:  Table [Voo_Reserva]

CREATE TABLE IF NOT EXISTS [Voo_Reserva](
	[ID_Voo] INTEGER
	[ID_Reserva] INTEGER NOT NULL
);
