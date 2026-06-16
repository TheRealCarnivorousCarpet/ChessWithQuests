```mermaid
classDiagram
    %% Core Enums
    class Barva {
        <<enumeration>>
        BILY
        CERNY
        __str__() str
    }

    class TypTahu {
        <<enumeration>>
        NORMALNI
        UTOK
        EN_PASSANT
        DLOUHA_ROSADA
        KRATKA_ROSADA
        __str__() str
    }

    class NotationType {
        <<enumeration>>
        SINGLE_LETTER
    }

    %% Base Classes & Constants
    class Pole {
        +str souradnice
        +int sloupec
        +int rada
        +SLOUPCE$ str
        +RADY$ str
        +from_sloupec_rada(s: int, r: int)$ Pole
        +value() str
    }

    class Tah {
        +Pole vychozi_pole
        +Pole cilova_pole
        +Figurka figurka
        +TypTahu typ_tahu
        +over_platnost() bool
        +proved()
    }

    %% Figures and Inheritance
    class Figurka {
        <<abstract>>
        +str jmeno
        +str jmeno_kratke
        +Barva barva
        +int n_kroku
        +bool hopper
        +bool was_moved
        +set~Vektor~ vektor
        +set~Vektor~ vektor_utoku
        +get_smery() set~Vektor~
        +get_smery_utoku() set~Vektor~
        +muze_tahat(od: Pole, do: Pole, typ_tahu: TypTahu) bool
        +mezikroky(od: Pole, do: Pole, typ_tahu: TypTahu) list~Pole~
    }

    class Kral {
        +muze_tahat(od: Pole, do: Pole, typ_tahu: TypTahu) bool
        +mezikroky(od: Pole, do: Pole, typ_tahu: TypTahu) list~Pole~
    }
    class Dama
    class Strelec
    class Kun
    class Vez {
        +muze_tahat(od: Pole, do: Pole, typ_tahu: TypTahu) bool
        +mezikroky(od: Pole, do: Pole, typ_tahu: TypTahu) list~Pole~
    }
    class Pesak {
        +muze_tahat(od: Pole, do: Pole, typ_tahu: TypTahu) bool
        +mezikroky(od: Pole, do: Pole, typ_tahu: TypTahu) list~Pole~
    }

    Figurka <|-- Kral
    Figurka <|-- Dama
    Figurka <|-- Strelec
    Figurka <|-- Kun
    Figurka <|-- Vez
    Figurka <|-- Pesak

    Figurka --> Barva : barva

    %% Board and Management
    class HerniPlocha {
        +list~Figurka~ vyhozene_figurky_b
        +list~Figurka~ vyhozene_figurky_c
        +tuple~int,int~ rozmery
        +vrat_obsah(pole: Pole) Figurka
        +posun_figurky(tah: Tah) bool
        +nahrad_figurku(figurka: Figurka, tah: Tah)
    }

    class GameManager {
        +HerniPlocha plocha
        +int activni_hrac
        +list~Hrac~ hraci
        +Tah actualni_tah
        +GameTimer casovac
        +GameLogger game_logger
        +proved_tah() bool
        +zacni_tah() Tah
        +mozne_tahy() list~Tah~
        +zrus_tah()
        +ulos_log()
        +najdi_uzivatele(i: int) Uzivatel
    }

    class GameTimer {
        +list~Hrac~ cas_hrac
        +nuluj_cas()
        +pocitej_cas(hrac: int)
    }

    class RevizorTahu {
        +HerniPlocha plocha
        +Tah tah
        +simulovej_tah()
    }

    %% Logger Engine
    class GameLogger {
        +TextIOBase soubor
        +list~Tah~ log
        +uloz_tah(tah: Tah)
        +vytvor_soubor(s: str)
    }

    class ChessNotationWriter {
        +NotationType typ
        +item()
    }

    class ExportWriter {
        +field
    }

    class MetadataWriter {
        +method(xxx)
    }

    %% User & Progression System
    class Hrac {
        +Barva barva
        +Uzivatel uzivatel
        +get_elo_rating() int
    }

    class Uzivatel {
        +str uzivatelske_jmeno
        +str jmeno
        +str email
        +int elo
        +list~Kwest~ splnene_kwesty
        +pridej_kwest(kwest: Kwest)
    }

    class Kwest {
        +str nazev
        +str popis
        +over() bool
    }

    class KwestManager {
        +field
        +method(xxx)
    }

    %% Structural System Interactions / Associations
    Tah --> Pole : vychozi_pole
    Tah --> Pole : cilova_pole
    Tah --> Figurka : figurka
    Tah --> TypTahu : typ_tahu

    GameManager --> HerniPlocha : plocha
    GameManager --> GameTimer : casovac
    GameManager --> GameLogger : game_logger
    GameManager --> Hrac : hraci
    GameManager --> Tah : actualni_tah

    GameTimer --> Hrac : cas_hrac
    RevizorTahu --> HerniPlocha : plocha
    RevizorTahu --> Tah : tah
    GameLogger --> Tah : log
    ChessNotationWriter --> NotationType : typ

    Hrac --> Barva : barva
    Hrac --> Uzivatel : uzivatel
    Uzivatel --> Kwest : splnene_kwesty
