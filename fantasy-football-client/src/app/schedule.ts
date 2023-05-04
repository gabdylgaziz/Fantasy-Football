export interface Game {
    team1: string;
    team1Src: string;
    team1g: number;
    team2: string;
    team2Src: string;
    team2g: number;
    time: string;
}

export interface GameDate{
    day: string;
}

export interface GameSch{
    date: GameDate;
    game: Game[];
}

export const Games = [
    {
        date: {
            day: "Wednesday 26 April",
        },
        game: [
            {
                team1: "WOL",
                team1Src: "assets/images/team-logos/woolver.png",
                team1g: 2,
                team2: "CRY",
                team2Src: "assets/images/team-logos/palace.png",
                team2g: 0,
                time: "00:30"
            },
            {
                team1: "AVL",
                team1Src: "assets/images/team-logos/aston.png",
                team1g: 1,
                team2: "FUL",
                team2Src: "assets/images/team-logos/fullham.png",
                team2g: 0,
                time: "00:30"
            },
            {
                team1: "LEE",
                team1Src: "assets/lee.png",
                team1g: 1,
                team2: "LEI",
                team2Src: "assets/lei.png",
                team2g: 1,
                time: "00:30"
            },
        ]
    },
    {
        date: {
            day: "Thursday 27 April"
        },
        game: [
            {
                team1: "NFO",
                team1Src: "assets/nfo.png",
                team1g: -1,
                team2: "BHA",
                team2Src: "assets/bha.png",
                team2g: -1,
                time: "00:30"
            },
            {
                team1: "CHE",
                team1Src: "assets/che.png",
                team1g: -1,
                team2: "BRE",
                team2Src: "assets/bre.png",
                team2g: -1,
                time: "00:45"
            },
            {
                team1: "WHU",
                team1Src: "assets/whu.png",
                team1g: -1,
                team2: "LIV",
                team2Src: "assets/liv.png",
                team2g: -1,
                time: "00:45"
            },
            {
                team1: "MCI",
                team1Src: "assets/mci.png",
                team1g: -1,
                team2: "ARS",
                team2Src: "assets/ars.png",
                team2g: -1,
                time: "01:00"
            },
        ]
    },
    {
        date: {
            day: "Friday 28 April"
        },
        game: [
            {
                team1: "EVE",
                team1Src: "assets/eve.png",
                team1g: -1,
                team2: "NEW",
                team2Src: "assets/new.png",
                team2g: -1,
                time: "00:45"
            },
            {
                team1: "SOU",
                team1Src: "assets/sou.png",
                team1g: -1,
                team2: "BOU",
                team2Src: "assets/bou.png",
                team2g: -1,
                time: "00:45"
            },
            {
                team1: "TOT",
                team1Src: "assets/tot.png",
                team1g: -1,
                team2: "MUN",
                team2Src: "assets/mun.png",
                team2g: -1,
                time: "01:15"
            },
        ]
    },
    
]