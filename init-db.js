db = db.getSiblingDB("condorcy");

db.createUser({
  user: "root",
  pwd: "pass",
  roles: [{ role: "readWrite", db: "condorcy" }],
});

db.users.insertMany([
  {
    id: "820f5a55-24af-4130-be47-574059d59436",
    pseudo: "Maryse_Balistreri",
    password: "sQDk2VpzVgtN7ol",
    date_of_birth: "1961-01-01",
    addresse: "34591 Carroll River",
    job: "National Markets Liaison",
    admin: true,
  },
  {
    id: "a4ef0bf3-aaf4-48fd-a028-963b29107b1a",
    pseudo: "Eli.Aufderhar-Fadel22",
    password: "7MHQdWswmxfonLv",
    date_of_birth: "1958-01-01",
    addresse: "49276 Nader Inlet",
    job: "District Web Director",
    admin: true,
  },
  {
    id: "b66fe6f4-19ea-49c0-b278-31a608da485f",
    pseudo: "Crawford_Strosin",
    password: "XgZz7QgmPmTaw8r",
    date_of_birth: "1953-01-01",
    addresse: "21538 Fourth Avenue",
    job: "Global Accounts Developer",
    admin: false,
  },
  {
    id: "b8c5b850-518d-4536-89c3-9e8a1526a8f5",
    pseudo: "Mark69",
    password: "AnZ764GSApJeSdB",
    date_of_birth: "1979-01-01",
    addresse: "28538 Hailie Walk",
    job: "International Group Consultant",
    admin: true,
  },
  {
    id: "1c136783-769f-460b-96bf-b7d7273266eb",
    pseudo: "Adelbert.Cummerata",
    password: "cBhobRu0N_QWFho",
    date_of_birth: "1960-01-01",
    addresse: "859 S Union Street",
    job: "National Optimization Planner",
    admin: false,
  },
  {
    id: "ea37eb9b-0d60-413d-84b0-c4df8cf5f12b",
    pseudo: "Lucious_Kihn",
    password: "LUhAo06j4tZzPaf",
    date_of_birth: "2001-01-01",
    addresse: "91940 Dejon Pine",
    job: "Human Markets Designer",
    admin: true,
  },
  {
    id: "17d0642e-0af9-48af-a441-fabb709813d7",
    pseudo: "Toney31",
    password: "b7ETRTx1HP44g6W",
    date_of_birth: "1969-01-01",
    addresse: "26870 Bay Street",
    job: "Global Implementation Producer",
    admin: true,
  },
  {
    id: "281d2248-0c17-45b9-9e96-10958f03593b",
    pseudo: "Kristofer.Von",
    password: "WGKrwQeuIP0VMBK",
    date_of_birth: "1953-01-01",
    addresse: "25412 Gottlieb Walk",
    job: "Lead Web Associate",
    admin: false,
  },
  {
    id: "a4d6d274-bfa4-4e38-b897-1aa310e2ff8a",
    pseudo: "Lenny31",
    password: "ct8gZRjrSLHYjA8",
    date_of_birth: "1978-01-01",
    addresse: "257 Leuschke Courts",
    job: "Global Marketing Liaison",
    admin: true,
  },
  {
    id: "11d085e4-09f6-4eaf-92de-c38cf3f6c6a1",
    pseudo: "Geo86",
    password: "M5Ngu3d7xtE_JSb",
    date_of_birth: "1975-01-01",
    addresse: "337 High Street",
    job: "Corporate Operations Administrator",
    admin: false,
  },
  {
    id: "73fb90ba-7a6d-44ea-bdeb-261d625635f1",
    pseudo: "Erwin.Wisoky47",
    password: "HEOELyeYk7tTZXd",
    date_of_birth: "1979-01-01",
    addresse: "838 Lester Skyway",
    job: "Customer Functionality Representative",
    admin: true,
  },
  {
    id: "8cf4a858-f606-4959-a184-19b60e38729a",
    pseudo: "Alicia28",
    password: "qvXtkMa7CbFb2pa",
    date_of_birth: "1969-01-01",
    addresse: "445 Maynard Path",
    job: "National Assurance Engineer",
    admin: true,
  },
  {
    id: "ac9f0f16-5fce-495a-91f1-d6e91b3f1e68",
    pseudo: "Coleman1",
    password: "9EY1jZ565bGAOE8",
    date_of_birth: "1956-01-01",
    addresse: "40966 Common Lane",
    job: "Central Brand Officer",
    admin: false,
  },
  {
    id: "27f9201d-41b8-41ee-aa23-f34647163da7",
    pseudo: "Ladarius.Kessler75",
    password: "GAKpfaXyMupvaic",
    date_of_birth: "1989-01-01",
    addresse: "2455 Cummerata Shores",
    job: "National Directives Designer",
    admin: true,
  },
  {
    id: "69f248e1-c635-4dfd-acd7-4f8918e117b4",
    pseudo: "Ryley44",
    password: "pBdYwKy9QgLF5jQ",
    date_of_birth: "1990-01-01",
    addresse: "934 Bosco Row",
    job: "Direct Directives Designer",
    admin: true,
  },
  {
    id: "d3e11ab8-2fcd-4e43-9de3-03d55118ffdb",
    pseudo: "Joel.Stark37",
    password: "EtTVI5PlVV9pVV5",
    date_of_birth: "1960-01-01",
    addresse: "22857 Hyatt Points",
    job: "Direct Communications Officer",
    admin: false,
  },
  {
    id: "e7e9bcfe-2db4-415d-889c-72f253ab79d4",
    pseudo: "Kavon.Hessel",
    password: "c9Xmif6_XU1NI1q",
    date_of_birth: "1989-01-01",
    addresse: "28611 Linda Park",
    job: "Forward Data Technician",
    admin: false,
  },
  {
    id: "7bbc569f-b98f-4b2a-9149-e981b28a3a6a",
    pseudo: "Orville29",
    password: "xXCafSLzbP16bOK",
    date_of_birth: "1977-01-01",
    addresse: "15125 Wilma Rest",
    job: "Product Directives Producer",
    admin: true,
  },
  {
    id: "6fb68895-050a-4cfc-a25c-672a8861fe6f",
    pseudo: "Jeffry14",
    password: "hgcC_W7T2mEvnH2",
    date_of_birth: "1964-01-01",
    addresse: "79851 Casper Fork",
    job: "Legacy Interactions Planner",
    admin: false,
  },
  {
    id: "38d94938-43a7-4c16-aa58-b60d60363edb",
    pseudo: "Eliezer.Pacocha77",
    password: "ozIElTRIrZCwIPI",
    date_of_birth: "1950-01-01",
    addresse: "5102 Mount Pleasant",
    job: "International Paradigm Officer",
    admin: true,
  },
  {
    id: "ea981798-1546-405c-afd5-99d6fb072a2a",
    pseudo: "Leon_Brekke",
    password: "ZRj5DqA_APBERI2",
    date_of_birth: "1993-01-01",
    addresse: "3367 Stiedemann Lock",
    job: "Principal Group Administrator",
    admin: true,
  },
  {
    id: "a2d8ff5b-add0-48de-afec-0b9bf187e260",
    pseudo: "Alena_Walker",
    password: "3VqZN5D74934xxp",
    date_of_birth: "1959-01-01",
    addresse: "7157 Warren Road",
    job: "Human Assurance Developer",
    admin: false,
  },
  {
    id: "bc7177de-d40d-4978-917f-4624d7cc2879",
    pseudo: "Kaya_Moore91",
    password: "vbftjuey2ogwbgK",
    date_of_birth: "1991-01-01",
    addresse: "544 Manor Way",
    job: "Legacy Creative Director",
    admin: true,
  },
  {
    id: "f1cbb17b-6584-49e8-822c-602a4b7cd530",
    pseudo: "Seamus_Connelly",
    password: "r7uE9S6uv4Jc1sZ",
    date_of_birth: "1960-01-01",
    addresse: "458 Hahn Mount",
    job: "International Security Consultant",
    admin: false,
  },
  {
    id: "41de043a-722c-4d3e-be52-fad9f78b0f72",
    pseudo: "Elyssa37",
    password: "NKuWo9tqIzNcegB",
    date_of_birth: "1951-01-01",
    addresse: "12938 Ebert Lock",
    job: "District Research Representative",
    admin: true,
  },
  {
    id: "5ffbf263-fd57-4933-ae11-5903a81410ae",
    pseudo: "Americo79",
    password: "xMYsypmkMZODzbN",
    date_of_birth: "1965-01-01",
    addresse: "3686 Charles Street",
    job: "Regional Mobility Agent",
    admin: true,
  },
  {
    id: "fe885170-5f83-49e0-84d6-9363a456574a",
    pseudo: "Wallace_Towne",
    password: "wGnUrc6PEvJM7Ad",
    date_of_birth: "1999-01-01",
    addresse: "678 Elian Roads",
    job: "Legacy Response Administrator",
    admin: true,
  },
  {
    id: "3951ee22-c4bc-472c-befb-25d1ed2751de",
    pseudo: "Mavis_Tremblay61",
    password: "St_gd8AoYRdwyE2",
    date_of_birth: "1962-01-01",
    addresse: "955 Bergnaum Garden",
    job: "Senior Factors Liaison",
    admin: false,
  },
  {
    id: "ea93c504-0db9-46b4-a678-a9c39f79404c",
    pseudo: "Herminia.Daniel",
    password: "mK0FRHcPCVkRY7h",
    date_of_birth: "1984-01-01",
    addresse: "597 Jillian Skyway",
    job: "Future Interactions Supervisor",
    admin: false,
  },
  {
    id: "e255a04c-f8f5-4b01-abae-13479342905c",
    pseudo: "Hope.Bechtelar48",
    password: "c_cV8lZlRu32_8V",
    date_of_birth: "1967-01-01",
    addresse: "24478 University Avenue",
    job: "Senior Tactics Representative",
    admin: true,
  },
  {
    id: "129852df-0ab6-4e29-b4c3-e1208fdb5648",
    pseudo: "Kayli.Paucek",
    password: "5krUpAFudoJM9jU",
    date_of_birth: "2005-01-01",
    addresse: "66123 E Cedar Street",
    job: "Senior Group Associate",
    admin: false,
  },
  {
    id: "e663d59d-1cf3-4523-b024-a34a51595716",
    pseudo: "Zella21",
    password: "doHuGiDBPzHT8Xr",
    date_of_birth: "1973-01-01",
    addresse: "412 Dare Tunnel",
    job: "Direct Accountability Agent",
    admin: true,
  },
  {
    id: "8c9e3ed3-e858-4132-99d3-72b7dfe41bc7",
    pseudo: "Pearlie81",
    password: "GBWFBjEAPGYtqn1",
    date_of_birth: "1984-01-01",
    addresse: "82979 Harvey Mews",
    job: "Human Group Designer",
    admin: false,
  },
  {
    id: "1f03ea31-1f3b-4af7-8e54-f18e2a5beab8",
    pseudo: "Lukas_Muller",
    password: "07Vpiutc1u70uMi",
    date_of_birth: "1991-01-01",
    addresse: "12327 S Union Street",
    job: "Product Communications Associate",
    admin: true,
  },
  {
    id: "90588e11-ac8e-49de-8b64-db5f9fb0cd48",
    pseudo: "Garth.Reilly78",
    password: "_sHqltUqmwevgX3",
    date_of_birth: "1990-01-01",
    addresse: "616 Moses Well",
    job: "Lead Accounts Specialist",
    admin: false,
  },
  {
    id: "6ea85a3f-7754-46f4-b824-4c70d9489d3f",
    pseudo: "Adell.MacGyver",
    password: "HZzibsZAwyAnoNK",
    date_of_birth: "1973-01-01",
    addresse: "160 Judd Fall",
    job: "Corporate Functionality Orchestrator",
    admin: true,
  },
  {
    id: "645c915c-a798-4fab-b44c-56f841fe05f0",
    pseudo: "Sarina49",
    password: "dvrccgI4xNnEiDu",
    date_of_birth: "1961-01-01",
    addresse: "896 Adeline Common",
    job: "Global Intranet Executive",
    admin: true,
  },
  {
    id: "38e7d99f-65fc-4d87-9f8d-530554beef0b",
    pseudo: "Matteo97",
    password: "GiADfW7h3qBbXS3",
    date_of_birth: "1979-01-01",
    addresse: "93241 Pfeffer Falls",
    job: "Regional Research Representative",
    admin: true,
  },
  {
    id: "46801e54-56b1-4191-8912-757a1b8424e8",
    pseudo: "Bonnie21",
    password: "e6ShhiqCnoxB0HV",
    date_of_birth: "1998-01-01",
    addresse: "783 Mount Pleasant",
    job: "Investor Accountability Director",
    admin: false,
  },
  {
    id: "3378ac40-afc8-417e-b7b1-c521f842e2a8",
    pseudo: "Stefanie.Wilkinson75",
    password: "Kvo4zYHuFitDfvZ",
    date_of_birth: "1954-01-01",
    addresse: "911 Bradley Passage",
    job: "Corporate Optimization Administrator",
    admin: true,
  },
  {
    id: "5edc5278-64d3-4b1f-a695-60c4ecaf2c9f",
    pseudo: "Max.DAmore-Hickle7",
    password: "4z2JdnWwrbg2bvf",
    date_of_birth: "1966-01-01",
    addresse: "36034 Carolyn Court",
    job: "Investor Implementation Specialist",
    admin: true,
  },
  {
    id: "ca51ebd2-0096-4698-ab4e-78026188be6a",
    pseudo: "Blaze_Kuhlman",
    password: "lXPf1RwA6wPeqQ9",
    date_of_birth: "1964-01-01",
    addresse: "9099 S Center Street",
    job: "Internal Data Technician",
    admin: false,
  },
  {
    id: "b746895a-ee0e-47c1-93ae-4cf979b5ee52",
    pseudo: "Hanna_Fahey75",
    password: "E9F0sZGwPWt8leO",
    date_of_birth: "1960-01-01",
    addresse: "17589 S Center Street",
    job: "Chief Program Executive",
    admin: false,
  },
  {
    id: "9190cd21-d512-4164-bb19-68c4dbe38ae3",
    pseudo: "Queenie13",
    password: "sXXEWNtG5ZFykn8",
    date_of_birth: "1943-01-01",
    addresse: "9664 Church Avenue",
    job: "Dynamic Marketing Engineer",
    admin: false,
  },
  {
    id: "4322451a-7425-4e33-aa61-13ba906ebc1d",
    pseudo: "Hilario_Grimes-Weissnat13",
    password: "5T1UY6Zgl5cTvnK",
    date_of_birth: "1973-01-01",
    addresse: "52998 Vine Street",
    job: "Investor Metrics Director",
    admin: false,
  },
  {
    id: "6b95d36e-ea46-4f7c-ad6d-90afbc64e72a",
    pseudo: "Chasity.Bogan49",
    password: "ZW6usnnX94eCbrw",
    date_of_birth: "1976-01-01",
    addresse: "5707 Jamil Flat",
    job: "Product Accountability Assistant",
    admin: false,
  },
  {
    id: "8beceaee-6e64-4014-8d6c-088c547f5353",
    pseudo: "Jay_Harber",
    password: "kvw34BteADS25e5",
    date_of_birth: "1945-01-01",
    addresse: "72666 Delmer Bridge",
    job: "Legacy Functionality Engineer",
    admin: false,
  },
  {
    id: "a4a28a24-3fb0-4af9-a5d3-da2b5c2cb409",
    pseudo: "Constantin_Fadel",
    password: "QobUiAP2rUgOANK",
    date_of_birth: "1966-01-01",
    addresse: "580 Beier Ridges",
    job: "Future Infrastructure Assistant",
    admin: false,
  },
  {
    id: "b05baf69-7ee3-4995-9095-dd61b0f7af05",
    pseudo: "Salvador53",
    password: "0IoEuX9FX1SC5Kj",
    date_of_birth: "1988-01-01",
    addresse: "7939 Stehr Dale",
    job: "Direct Configuration Director",
    admin: true,
  },
  {
    id: "3844ec32-9c95-44a7-b397-36e275f6e8cd",
    pseudo: "Myriam.Okuneva",
    password: "_nJfIIEv0LgKpd_",
    date_of_birth: "1968-01-01",
    addresse: "9576 Mueller Camp",
    job: "Internal Accounts Architect",
    admin: true,
  },
  {
    id: "493f80f7-3734-42b3-90bf-f51dfcf7ba15",
    pseudo: "Wilburn24",
    password: "efV5wM7adVy8E5A",
    date_of_birth: "1950-01-01",
    addresse: "471 Cortez Hollow",
    job: "Lead Division Producer",
    admin: true,
  },
  {
    id: "a3edd517-2f3b-4742-a705-e7e672ce6c3e",
    pseudo: "Stephen.Boehm",
    password: "PPpEbXFU8O_qJZH",
    date_of_birth: "1945-01-01",
    addresse: "6476 Old Road",
    job: "Customer Tactics Manager",
    admin: true,
  },
  {
    id: "6992de94-bc99-4ad0-8659-05d7c63e0a5a",
    pseudo: "Maryam.Erdman40",
    password: "knbvg9dByRFhpRA",
    date_of_birth: "1977-01-01",
    addresse: "608 Monroe Street",
    job: "Lead Web Consultant",
    admin: true,
  },
  {
    id: "824c64d8-dace-40d7-b46b-68ec6638bbd7",
    pseudo: "Christiana74",
    password: "f7l453KpS4hXtCO",
    date_of_birth: "1981-01-01",
    addresse: "715 Addison Stravenue",
    job: "Global Functionality Executive",
    admin: false,
  },
  {
    id: "f479a6b9-1ade-466d-aa44-01ef0e8df1df",
    pseudo: "Xzavier.Towne",
    password: "NJcDCVNS287eznR",
    date_of_birth: "1997-01-01",
    addresse: "9072 Walsh Junctions",
    job: "Chief Data Associate",
    admin: true,
  },
  {
    id: "a9b10c6c-d848-4f40-8035-e7d54c3afa4f",
    pseudo: "Berry_Beahan13",
    password: "DAFBkzrOffSYkwq",
    date_of_birth: "1982-01-01",
    addresse: "94250 Walsh Rapids",
    job: "Direct Tactics Orchestrator",
    admin: false,
  },
  {
    id: "a3543c34-65bf-4ff4-9653-e460e83ef413",
    pseudo: "Kira94",
    password: "mvUQagDJXeInyTp",
    date_of_birth: "1943-01-01",
    addresse: "52025 Fore Street",
    job: "Direct Tactics Director",
    admin: true,
  },
  {
    id: "5b3e3971-3e36-4fb2-882c-6a7414ee071f",
    pseudo: "Jaylon45",
    password: "5t0e4YttAagGKpX",
    date_of_birth: "1996-01-01",
    addresse: "938 Nikita Spurs",
    job: "International Research Designer",
    admin: true,
  },
  {
    id: "8a7994a8-bb97-4aef-9cf9-48853b5de62e",
    pseudo: "Abigale_Harris",
    password: "zgcG1EXDJm0jTzM",
    date_of_birth: "1945-01-01",
    addresse: "735 Maple Street",
    job: "Legacy Creative Coordinator",
    admin: true,
  },
  {
    id: "9fcccc48-0903-4d5c-bebb-4651661a72f6",
    pseudo: "Eunice90",
    password: "B8Dnjlsz0MdIbJr",
    date_of_birth: "2003-01-01",
    addresse: "654 The Laurels",
    job: "Corporate Solutions Manager",
    admin: true,
  },
  {
    id: "bc8a95b8-124e-4f22-a72a-a892d64fc512",
    pseudo: "Darron.Treutel",
    password: "iE5cbegHmoG4cdc",
    date_of_birth: "1990-01-01",
    addresse: "2677 O'Connell Circles",
    job: "Forward Brand Executive",
    admin: true,
  },
  {
    id: "358de4b2-884f-4860-be78-3291c6b515db",
    pseudo: "Matilda_Rolfson",
    password: "4TnL4KiM2tRFRMw",
    date_of_birth: "1994-01-01",
    addresse: "91838 N Main Avenue",
    job: "Customer Creative Strategist",
    admin: false,
  },
  {
    id: "7d7b8205-bdd3-48f6-a518-8b95989053d5",
    pseudo: "Bobbie_Ritchie63",
    password: "5gEZiKH4Ax23y8f",
    date_of_birth: "1965-01-01",
    addresse: "5445 Brakus Wall",
    job: "Corporate Paradigm Representative",
    admin: false,
  },
  {
    id: "111f3772-912b-4c6d-b714-0d17ec606f67",
    pseudo: "Cydney.Hoeger84",
    password: "mHdw8j6yThefO33",
    date_of_birth: "1987-01-01",
    addresse: "589 Walter Isle",
    job: "Senior Directives Producer",
    admin: true,
  },
  {
    id: "b6b70539-99c5-49db-bdc2-7b1435ffcc6b",
    pseudo: "Liza35",
    password: "Yr668blqJ23s36W",
    date_of_birth: "1978-01-01",
    addresse: "149 E 7th Street",
    job: "Central Research Architect",
    admin: true,
  },
  {
    id: "baf6a3db-a03e-40b3-8680-bd5d03e82be5",
    pseudo: "Amelia6",
    password: "HfUzStO6SDFPuls",
    date_of_birth: "1979-01-01",
    addresse: "297 Larch Close",
    job: "International Functionality Liaison",
    admin: true,
  },
  {
    id: "6ebb8495-2a7c-4725-a965-31ef9669697f",
    pseudo: "Valentine_Yost",
    password: "SrHf5OGjBMjTc8j",
    date_of_birth: "1996-01-01",
    addresse: "229 Jennie Lodge",
    job: "National Applications Director",
    admin: true,
  },
  {
    id: "d83ea197-7cbf-40bf-91ce-9c212dcbf53e",
    pseudo: "Violette.Goldner55",
    password: "YtzKlYtferEkZXf",
    date_of_birth: "1984-01-01",
    addresse: "6887 Annamarie Alley",
    job: "Chief Configuration Developer",
    admin: true,
  },
  {
    id: "7b958c67-2a3e-4df6-943a-75658631be48",
    pseudo: "Dahlia.Strosin",
    password: "sN46Xeewbzwh7Is",
    date_of_birth: "1958-01-01",
    addresse: "8401 Poplar Close",
    job: "Dynamic Accounts Liaison",
    admin: false,
  },
  {
    id: "61d95ab7-6b82-49ba-adb2-e3cce48c8753",
    pseudo: "Lauretta_Olson39",
    password: "y_zy4eKTIGhpkoq",
    date_of_birth: "1952-01-01",
    addresse: "1519 S 9th Street",
    job: "Investor Security Consultant",
    admin: false,
  },
  {
    id: "d4edb873-2ae7-4daf-8bf6-b11ed9e1cd32",
    pseudo: "Bernice98",
    password: "5elF8kcO6Ocy_qi",
    date_of_birth: "1964-01-01",
    addresse: "9575 Greyson Lane",
    job: "Chief Security Architect",
    admin: true,
  },
  {
    id: "b8a09a8d-629a-4366-972d-1e3afbdffb94",
    pseudo: "Meredith.Douglas",
    password: "4vlu0qVxlY3pNgj",
    age: 40,
    addresse: "2352 Heron Close",
    job: "Internal Web Designer",
    admin: true,
  },
  {
    id: "fb53ee50-443b-4c1a-a60b-9bc704326d74",
    pseudo: "Maddison.Walter",
    password: "klt0GVsfsxkdkf4",
    age: 47,
    addresse: "164 Clifton Pike",
    job: "Chief Accounts Administrator",
    admin: false,
  },
  {
    id: "c1b34415-5fab-4453-bcae-644161604e43",
    pseudo: "Stevie14",
    password: "xjqnuYPD_TKXWaw",
    age: 79,
    addresse: "9824 Felicita Place",
    job: "Legacy Brand Architect",
    admin: true,
  },
  {
    id: "06d963fb-91f4-4a23-9412-aa84c3ff49dc",
    pseudo: "Alan82",
    password: "sNVBl7um4alNZA3",
    age: 76,
    addresse: "98534 Cummerata Fords",
    job: "Global Communications Liaison",
    admin: true,
  },
  {
    id: "7902b34a-ac75-4699-884a-59bdd6a75ad9",
    pseudo: "Jaydon_Ullrich",
    password: "bGOuO4uJhOieQEE",
    age: 64,
    addresse: "471 N Court Street",
    job: "Product Data Producer",
    admin: false,
  },
  {
    id: "cd5bc8d3-ba8c-460b-96b4-e6fd70909c89",
    pseudo: "Liza.Bradtke65",
    password: "9IEqUKibfz4etAZ",
    age: 43,
    addresse: "163 Tennyson Road",
    job: "International Implementation Designer",
    admin: true,
  },
  {
    id: "e79a9f76-89f0-41bd-98d9-ab4a05ee845c",
    pseudo: "Sim_Parisian67",
    password: "XETLFbJdvDkcmpQ",
    age: 40,
    addresse: "9692 Bettye Avenue",
    job: "Senior Research Producer",
    admin: false,
  },
  {
    id: "579a4e5f-118a-4b0a-8f4b-491fde29fe2d",
    pseudo: "Joshuah62",
    password: "rU0k_dF6Brwd9Xq",
    age: 39,
    addresse: "814 Clarendon Road",
    job: "Future Implementation Manager",
    admin: false,
  },
  {
    id: "d41b3234-e1a4-4695-b048-d2374adc7127",
    pseudo: "Myriam.DuBuque",
    password: "asyr5LoTpOkWXHq",
    age: 60,
    addresse: "37828 Romaguera Stream",
    job: "National Usability Officer",
    admin: true,
  },
  {
    id: "e26f0b9a-2c61-4ddc-b22d-152eaebd8ce0",
    pseudo: "Reid_Greenfelder-Williamson84",
    password: "keO6outycG1Lkpi",
    age: 23,
    addresse: "887 Lakin Points",
    job: "Investor Markets Manager",
    admin: true,
  },
  {
    id: "7e1932f4-f717-4024-aa09-8d48f47ed68e",
    pseudo: "Ricardo_Feeney33",
    password: "3CNy0TPyo9mO2cK",
    age: 79,
    addresse: "8518 Maria Garden",
    job: "Global Group Manager",
    admin: true,
  },
  {
    id: "5b2d22fd-3474-4158-a928-e5a08946b58e",
    pseudo: "Jody_Bins",
    password: "C9Ov4slrsytwjzv",
    age: 31,
    addresse: "84752 Angeline Extension",
    job: "Corporate Security Developer",
    admin: false,
  },
  {
    id: "636d235c-e9e2-4fde-88f4-4f152132efb5",
    pseudo: "Julie.Sipes97",
    password: "tHr0rQCybNVm_yC",
    age: 65,
    addresse: "199 Margret Valleys",
    job: "Central Tactics Facilitator",
    admin: true,
  },
  {
    id: "44d104b5-0958-4ee8-acab-f5f05e860a63",
    pseudo: "Clair_Schulist-Wunsch",
    password: "RaQRjgZwUyYi3T9",
    age: 75,
    addresse: "937 Bins Spur",
    job: "Investor Integration Designer",
    admin: false,
  },
  {
    id: "085107cc-d28a-4644-a769-7fa3f29cee21",
    pseudo: "Juanita94",
    password: "_V9zOq2nlMBHcmD",
    age: 66,
    addresse: "646 Laburnum Grove",
    job: "Internal Accounts Strategist",
    admin: false,
  },
  {
    id: "e24541c2-8d86-4b2e-b631-73037fed61c3",
    pseudo: "Andy_OKeefe89",
    password: "zMrUYvD6rS6ORQo",
    age: 20,
    addresse: "31255 Eulalia Pass",
    job: "Senior Accountability Coordinator",
    admin: false,
  },
  {
    id: "410b0252-98cb-472a-8a1e-7ee2e0c55622",
    pseudo: "Allen_Sauer97",
    password: "ENQWEOOf3BH9hyG",
    age: 44,
    addresse: "6661 Anais Fields",
    job: "Legacy Functionality Strategist",
    admin: true,
  },
  {
    id: "d777a9c3-60fd-4801-8e0b-5200e6b7c1b6",
    pseudo: "Adaline14",
    password: "bJGOPw_zfTd9Evi",
    age: 19,
    addresse: "4576 Kings Highway",
    job: "Forward Quality Officer",
    admin: true,
  },
  {
    id: "238711e4-3031-4a4b-92fe-a3eeed56145c",
    pseudo: "Abraham.Larkin",
    password: "0JzXe0oqWXyVuJn",
    age: 51,
    addresse: "19990 Robin Fall",
    job: "Customer Implementation Manager",
    admin: true,
  },
  {
    id: "04ab1b85-9add-4186-9480-90aca4caa264",
    pseudo: "Jane.Senger67",
    password: "8_l_j2epCYGGKrI",
    age: 34,
    addresse: "152 Manor Drive",
    job: "Corporate Integration Architect",
    admin: true,
  },
  {
    id: "b6bf4fdf-6168-4d74-8671-a396ec5cbf33",
    pseudo: "Jakayla19",
    password: "vC9mR6voyU9wqMA",
    age: 55,
    addresse: "612 S 14th Street",
    job: "Senior Response Associate",
    admin: false,
  },
  {
    id: "afe13d88-c873-423c-8d14-6625cb53669c",
    pseudo: "Scottie10",
    password: "4jUnrj5G34gp8l7",
    age: 18,
    addresse: "98418 McDermott Camp",
    job: "Central Operations Engineer",
    admin: true,
  },
  {
    id: "1009d757-d5a5-43b4-831d-7cf145a3b143",
    pseudo: "Brian26",
    password: "iDYikE37C_fvzHo",
    age: 73,
    addresse: "790 Eudora Isle",
    job: "Senior Tactics Supervisor",
    admin: true,
  },
  {
    id: "baacb4b2-e61c-480e-84b1-348b8c313822",
    pseudo: "Hadley_Runolfsson-Reichel",
    password: "6JHbXgVyQ_RoQKN",
    age: 74,
    addresse: "62841 Shawna Loop",
    job: "Principal Accountability Officer",
    admin: false,
  },
  {
    id: "65ff16f5-ab8c-4dbe-8a28-c5b803103d9d",
    pseudo: "Mona_Bruen94",
    password: "I4FpGl6rqhDAq9E",
    age: 45,
    addresse: "27345 Ash Road",
    job: "Legacy Division Executive",
    admin: true,
  },
  {
    id: "dfffad44-2527-474b-abc5-95145f2c8fd7",
    pseudo: "Gino_Graham",
    password: "SEPnIQFlTBdBKyb",
    age: 24,
    addresse: "5928 North Avenue",
    job: "Principal Web Developer",
    admin: false,
  },
  {
    id: "82807b40-6d61-4bcb-9092-964f338f2193",
    pseudo: "Dewitt_Runolfsdottir",
    password: "Zsbk9_wdJ0APHMD",
    age: 23,
    addresse: "55786 Ebert Rapid",
    job: "Dynamic Branding Officer",
    admin: true,
  },
  {
    id: "65c41f64-5860-49c0-b1e7-821fbf4c73de",
    pseudo: "Herta_Schoen66",
    password: "tewurD4rUt2_i0F",
    age: 40,
    addresse: "24980 Rosenbaum Ways",
    job: "Dynamic Solutions Coordinator",
    admin: true,
  },
  {
    id: "34a42c48-5963-4947-8129-1a5a2e7e4d08",
    pseudo: "Vicente.Miller91",
    password: "eOGUeUTLrX9quDO",
    age: 72,
    addresse: "82450 Edwina Haven",
    job: "Customer Paradigm Facilitator",
    admin: false,
  },
]);

db.surveys.insertMany([
  {
    id: "survey-001",
    creator: {
      user_id: {
        $oid: "fb53ee50-443b-4c1a-a60b-9bc704326d74",
      },
    },
    question: "Impedit vel adopto cras degenero cum venia vix.",
    description:
      "Sui dolor nobis contego. Explicabo summa dolorum enim animi cubitum degero. Tergum supplanto somniculosus decretum aestas usque victoria.",
    date: {
      create: "2023-12-11",
      start: "2025-06-23",
      end: "2024-12-26",
      update: "2024-11-27",
    },
    choix: ["forgery", "netsuke", "understanding"],
    reponses: [],
    results: [],
  },
  {
    id: "survey-002",
    creator: {
      user_id: {
        $oid: "493f80f7-3734-42b3-90bf-f51dfcf7ba15",
      },
    },
    question: "Pariatur bellum xiphias a demulceo talis tendo tyrannus.",
    description:
      "Adulatio libero aveho voluptates sunt. Sumptus cuppedia fuga aranea pecus vicissitudo ulciscor pecco. Carcer claustrum velociter culpa tracto bellicus appello.",
    date: {
      create: "2024-09-11",
      start: "2025-05-11",
      end: "2025-04-11",
      update: "2024-11-27",
    },
    choix: ["skyscraper", "tenant", "ghost"],
    reponses: [
      {
        user_id: {
          $oid: "b8c5b850-518d-4536-89c3-9e8a1526a8f5",
        },
        reponse: ["ghost", "skyscraper", "tenant"],
      },
      {
        user_id: {
          $oid: "6ea85a3f-7754-46f4-b824-4c70d9489d3f",
        },
        reponse: ["ghost", "tenant"],
      },
      {
        user_id: {
          $oid: "b6b70539-99c5-49db-bdc2-7b1435ffcc6b",
        },
        reponse: [],
      },
    ],
    results: [],
  },
  {
    id: "survey-003",
    creator: {
      user_id: {
        $oid: "b8c5b850-518d-4536-89c3-9e8a1526a8f5",
      },
    },
    question:
      "Dolorum volva titulus urbanus voluntarius claustrum bestia color.",
    description:
      "Soleo tabgo sordeo vulticulus. Alioqui ipsum attero decens vulgaris veritas conculco commodi adstringo. Dolorum ceno adeptio vulticulus abbas delego patrocinor.",
    date: {
      create: "2024-08-06",
      start: "2025-01-03",
      end: "2024-12-30",
      update: "2024-11-27",
    },
    choix: ["simple", "dish", "lay", "innovation"],
    reponses: [
      {
        user_id: {
          $oid: "fe885170-5f83-49e0-84d6-9363a456574a",
        },
        reponse: ["lay", "innovation", "dish"],
      },
      {
        user_id: {
          $oid: "cd5bc8d3-ba8c-460b-96b4-e6fd70909c89",
        },
        reponse: ["simple", "dish", "innovation"],
      },
      {
        user_id: {
          $oid: "5b2d22fd-3474-4158-a928-e5a08946b58e",
        },
        reponse: ["lay"],
      },
      {
        user_id: {
          $oid: "7902b34a-ac75-4699-884a-59bdd6a75ad9",
        },
        reponse: ["simple", "lay"],
      },
    ],
    results: [],
  },
  {
    id: "survey-004",
    creator: {
      user_id: {
        $oid: "493f80f7-3734-42b3-90bf-f51dfcf7ba15",
      },
    },
    question:
      "Cuppedia spectaculum ipsam corona quis sufficio doloremque caste.",
    description:
      "Minus odio summisse claudeo cognomen congregatio enim tres assumenda aspernatur. Damno triduana vinitor triumphus alioqui venio audio. Verecundia contra cogo conculco xiphias viridis.",
    date: {
      create: "2024-11-22",
      start: "2025-04-26",
      end: "2025-01-12",
      update: "2024-11-28",
    },
    choix: ["backburn", "slide", "netsuke", "exasperation"],
    reponses: [
      {
        user_id: {
          $oid: "9fcccc48-0903-4d5c-bebb-4651661a72f6",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "baf6a3db-a03e-40b3-8680-bd5d03e82be5",
        },
        reponse: ["netsuke", "exasperation", "slide", "backburn"],
      },
      {
        user_id: {
          $oid: "493f80f7-3734-42b3-90bf-f51dfcf7ba15",
        },
        reponse: ["netsuke", "slide"],
      },
      {
        user_id: {
          $oid: "a4a28a24-3fb0-4af9-a5d3-da2b5c2cb409",
        },
        reponse: ["exasperation", "backburn", "slide", "netsuke"],
      },
      {
        user_id: {
          $oid: "b8c5b850-518d-4536-89c3-9e8a1526a8f5",
        },
        reponse: ["slide", "backburn"],
      },
      {
        user_id: {
          $oid: "5edc5278-64d3-4b1f-a695-60c4ecaf2c9f",
        },
        reponse: ["slide", "netsuke", "exasperation", "backburn"],
      },
      {
        user_id: {
          $oid: "04ab1b85-9add-4186-9480-90aca4caa264",
        },
        reponse: ["slide", "netsuke", "backburn", "exasperation"],
      },
      {
        user_id: {
          $oid: "ea981798-1546-405c-afd5-99d6fb072a2a",
        },
        reponse: [],
      },
    ],
    results: [],
  },
  {
    id: "survey-005",
    creator: {
      user_id: {
        $oid: "9fcccc48-0903-4d5c-bebb-4651661a72f6",
      },
    },
    question:
      "Atqui apto conscendo desolo aeternus cometes congregatio dolorem.",
    description:
      "Ut demergo cogo aer doloribus. Curtus urbanus aureus. Antepono chirographum volva varius teres voveo.",
    date: {
      create: "2024-02-17",
      start: "2025-04-30",
      end: "2025-10-12",
      update: "2024-11-28",
    },
    choix: ["knitting", "nucleotidase", "steak", "suitcase", "newsletter"],
    reponses: [],
    results: [],
  },
  {
    id: "survey-006",
    creator: {
      user_id: {
        $oid: "9fcccc48-0903-4d5c-bebb-4651661a72f6",
      },
    },
    question: "Ciminatio cubicularis cibus tempus tollo suscipit conduco rem.",
    description:
      "Id quisquam in colligo cupressus avaritia accusamus. Culpa cunctatio accendo cervus depopulo delinquo. Tot vereor supra adstringo decerno concedo rem.",
    date: {
      create: "2024-06-09",
      start: "2025-11-09",
      end: "2024-12-26",
      update: "2024-11-28",
    },
    choix: ["wilderness", "nudge"],
    reponses: [
      {
        user_id: {
          $oid: "3951ee22-c4bc-472c-befb-25d1ed2751de",
        },
        reponse: ["nudge"],
      },
      {
        user_id: {
          $oid: "d41b3234-e1a4-4695-b048-d2374adc7127",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "645c915c-a798-4fab-b44c-56f841fe05f0",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "65ff16f5-ab8c-4dbe-8a28-c5b803103d9d",
        },
        reponse: ["nudge"],
      },
    ],
    results: [],
  },
  {
    id: "survey-007",
    creator: {
      user_id: {
        $oid: "afe13d88-c873-423c-8d14-6625cb53669c",
      },
    },
    question: "Surgo derelinquo cura quia verbum suppono tam aer.",
    description:
      "Ventosus coniuratio utilis pax spes volutabrum minus sequi. Ultio similique suasoria coniecto officiis solitudo. Demum demum triumphus quisquam valde odio tergeo trucido tergum.",
    date: {
      create: "2024-06-22",
      start: "2025-02-21",
      end: "2025-03-27",
      update: "2024-11-28",
    },
    choix: ["agreement", "expansion"],
    reponses: [
      {
        user_id: {
          $oid: "bc7177de-d40d-4978-917f-4624d7cc2879",
        },
        reponse: ["expansion"],
      },
      {
        user_id: {
          $oid: "baacb4b2-e61c-480e-84b1-348b8c313822",
        },
        reponse: ["expansion", "agreement"],
      },
      {
        user_id: {
          $oid: "820f5a55-24af-4130-be47-574059d59436",
        },
        reponse: ["agreement"],
      },
      {
        user_id: {
          $oid: "b6bf4fdf-6168-4d74-8671-a396ec5cbf33",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "6fb68895-050a-4cfc-a25c-672a8861fe6f",
        },
        reponse: ["agreement", "expansion"],
      },
      {
        user_id: {
          $oid: "06d963fb-91f4-4a23-9412-aa84c3ff49dc",
        },
        reponse: ["expansion", "agreement"],
      },
      {
        user_id: {
          $oid: "e79a9f76-89f0-41bd-98d9-ab4a05ee845c",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "afe13d88-c873-423c-8d14-6625cb53669c",
        },
        reponse: ["expansion"],
      },
    ],
    results: [],
  },
  {
    id: "survey-008",
    creator: {
      user_id: {
        $oid: "ea37eb9b-0d60-413d-84b0-c4df8cf5f12b",
      },
    },
    question: "Iusto viriliter atque arbustum aliquam abstergo textilis comis.",
    description:
      "Defessus statua amplitudo sulum debilito argentum. Conatus desipio aliquid delinquo tersus. Appello sursum versus recusandae suspendo sursum velum surculus veritatis tendo.",
    date: {
      create: "2024-08-30",
      start: "2025-11-12",
      end: "2025-07-30",
      update: "2024-11-28",
    },
    choix: ["sesame", "jungle", "guard", "editor", "taxicab"],
    reponses: [
      {
        user_id: {
          $oid: "e79a9f76-89f0-41bd-98d9-ab4a05ee845c",
        },
        reponse: ["editor", "jungle", "taxicab", "guard", "sesame"],
      },
      {
        user_id: {
          $oid: "41de043a-722c-4d3e-be52-fad9f78b0f72",
        },
        reponse: ["editor", "sesame", "jungle"],
      },
      {
        user_id: {
          $oid: "38e7d99f-65fc-4d87-9f8d-530554beef0b",
        },
        reponse: ["jungle", "sesame", "editor", "taxicab"],
      },
      {
        user_id: {
          $oid: "d777a9c3-60fd-4801-8e0b-5200e6b7c1b6",
        },
        reponse: ["taxicab", "guard", "sesame", "editor", "jungle"],
      },
      {
        user_id: {
          $oid: "06d963fb-91f4-4a23-9412-aa84c3ff49dc",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "824c64d8-dace-40d7-b46b-68ec6638bbd7",
        },
        reponse: ["taxicab", "editor", "guard", "jungle"],
      },
      {
        user_id: {
          $oid: "fe885170-5f83-49e0-84d6-9363a456574a",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "17d0642e-0af9-48af-a441-fabb709813d7",
        },
        reponse: ["guard", "sesame", "taxicab"],
      },
      {
        user_id: {
          $oid: "ca51ebd2-0096-4698-ab4e-78026188be6a",
        },
        reponse: ["editor", "taxicab", "jungle"],
      },
      {
        user_id: {
          $oid: "ac9f0f16-5fce-495a-91f1-d6e91b3f1e68",
        },
        reponse: ["sesame", "editor", "taxicab", "jungle"],
      },
    ],
    results: [],
  },
  {
    id: "survey-009",
    creator: {
      user_id: {
        $oid: "cd5bc8d3-ba8c-460b-96b4-e6fd70909c89",
      },
    },
    question:
      "Suscipio autem paens tergiversatio odit desparatus tondeo incidunt.",
    description:
      "Collum pecus defendo aperte talis repudiandae tabernus dolorem vivo tamquam. Sordeo utrum conforto campana quibusdam defluo celer combibo avarus. Depopulo sursum curvo accedo accusator careo.",
    date: {
      create: "2024-04-07",
      start: "2025-04-20",
      end: "2025-07-13",
      update: "2024-11-27",
    },
    choix: ["derby", "disconnection", "manner", "exploration"],
    reponses: [
      {
        user_id: {
          $oid: "129852df-0ab6-4e29-b4c3-e1208fdb5648",
        },
        reponse: ["disconnection", "exploration", "manner", "derby"],
      },
      {
        user_id: {
          $oid: "41de043a-722c-4d3e-be52-fad9f78b0f72",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "820f5a55-24af-4130-be47-574059d59436",
        },
        reponse: ["exploration", "derby", "disconnection", "manner"],
      },
      {
        user_id: {
          $oid: "69f248e1-c635-4dfd-acd7-4f8918e117b4",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "a4ef0bf3-aaf4-48fd-a028-963b29107b1a",
        },
        reponse: ["exploration", "manner", "derby", "disconnection"],
      },
    ],
    results: [],
  },
  {
    id: "survey-010",
    creator: {
      user_id: {
        $oid: "73fb90ba-7a6d-44ea-bdeb-261d625635f1",
      },
    },
    question: "Trado suggero rerum usque adsidue agnitio ascisco temptatio.",
    description:
      "Sonitus porro paulatim beatae adulescens cursim. Acies ocer desino truculenter libero. Admoveo quas amplitudo vulgaris ceno territo calcar caute cibus tollo.",
    date: {
      create: "2024-09-01",
      start: "2024-12-23",
      end: "2025-08-06",
      update: "2024-11-28",
    },
    choix: ["sightseeing", "embarrassment", "amendment", "procurement"],
    reponses: [
      {
        user_id: {
          $oid: "8c9e3ed3-e858-4132-99d3-72b7dfe41bc7",
        },
        reponse: ["amendment", "sightseeing", "procurement"],
      },
      {
        user_id: {
          $oid: "69f248e1-c635-4dfd-acd7-4f8918e117b4",
        },
        reponse: ["amendment"],
      },
      {
        user_id: {
          $oid: "5edc5278-64d3-4b1f-a695-60c4ecaf2c9f",
        },
        reponse: ["sightseeing", "procurement"],
      },
      {
        user_id: {
          $oid: "7902b34a-ac75-4699-884a-59bdd6a75ad9",
        },
        reponse: ["embarrassment"],
      },
      {
        user_id: {
          $oid: "238711e4-3031-4a4b-92fe-a3eeed56145c",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "e79a9f76-89f0-41bd-98d9-ab4a05ee845c",
        },
        reponse: ["sightseeing", "embarrassment", "procurement"],
      },
      {
        user_id: {
          $oid: "579a4e5f-118a-4b0a-8f4b-491fde29fe2d",
        },
        reponse: ["embarrassment", "amendment", "procurement"],
      },
    ],
    results: [],
  },
  {
    id: "survey-011",
    creator: {
      user_id: {
        $oid: "bc7177de-d40d-4978-917f-4624d7cc2879",
      },
    },
    question:
      "Civitas labore adulescens cruciamentum cunctatio paens iste carcer.",
    description:
      "Tabesco abeo convoco dignissimos ullus tredecim theologus. Decens necessitatibus auctus triduana. Sperno repudiandae tenetur.",
    date: {
      create: "2023-12-24",
      start: "2025-08-26",
      end: "2025-07-17",
      update: "2024-11-28",
    },
    choix: ["numeracy", "populist", "eyeliner", "equal"],
    reponses: [
      {
        user_id: {
          $oid: "27f9201d-41b8-41ee-aa23-f34647163da7",
        },
        reponse: ["numeracy", "populist"],
      },
      {
        user_id: {
          $oid: "61d95ab7-6b82-49ba-adb2-e3cce48c8753",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "d4edb873-2ae7-4daf-8bf6-b11ed9e1cd32",
        },
        reponse: ["numeracy", "populist"],
      },
      {
        user_id: {
          $oid: "6b95d36e-ea46-4f7c-ad6d-90afbc64e72a",
        },
        reponse: ["numeracy", "eyeliner", "equal"],
      },
      {
        user_id: {
          $oid: "34a42c48-5963-4947-8129-1a5a2e7e4d08",
        },
        reponse: ["numeracy", "eyeliner"],
      },
      {
        user_id: {
          $oid: "645c915c-a798-4fab-b44c-56f841fe05f0",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "a4a28a24-3fb0-4af9-a5d3-da2b5c2cb409",
        },
        reponse: ["populist", "numeracy"],
      },
      {
        user_id: {
          $oid: "65ff16f5-ab8c-4dbe-8a28-c5b803103d9d",
        },
        reponse: ["numeracy", "equal"],
      },
      {
        user_id: {
          $oid: "ea93c504-0db9-46b4-a678-a9c39f79404c",
        },
        reponse: ["eyeliner", "populist", "equal"],
      },
      {
        user_id: {
          $oid: "65c41f64-5860-49c0-b1e7-821fbf4c73de",
        },
        reponse: ["eyeliner", "numeracy"],
      },
    ],
    results: [],
  },
  {
    id: "survey-012",
    creator: {
      user_id: {
        $oid: "7bbc569f-b98f-4b2a-9149-e981b28a3a6a",
      },
    },
    question: "Adicio solum combibo bos rerum caste caelestis vulgivagus.",
    description:
      "Thorax aliquam ceno. Minus explicabo utrum neque deleniti terror cohaero tui. Caveo caelum calamitas amo.",
    date: {
      create: "2024-01-25",
      start: "2025-09-11",
      end: "2025-08-10",
      update: "2024-11-28",
    },
    choix: ["birth", "hygienic"],
    reponses: [],
    results: [],
  },
  {
    id: "survey-013",
    creator: {
      user_id: {
        $oid: "410b0252-98cb-472a-8a1e-7ee2e0c55622",
      },
    },
    question:
      "Contabesco vere veritatis amaritudo commodi villa animus degenero.",
    description:
      "Aspicio quos illo acquiro sono admoveo stips voluptatem tenus. Viriliter cunabula vilis curo aegrus cultellus speciosus avaritia animi. Damnatio succurro comedo debilito suasoria nisi.",
    date: {
      create: "2024-04-01",
      start: "2025-08-30",
      end: "2025-01-16",
      update: "2024-11-27",
    },
    choix: ["accelerator", "tapioca", "chasuble", "verve"],
    reponses: [
      {
        user_id: {
          $oid: "a3edd517-2f3b-4742-a705-e7e672ce6c3e",
        },
        reponse: ["verve", "tapioca", "accelerator"],
      },
      {
        user_id: {
          $oid: "8cf4a858-f606-4959-a184-19b60e38729a",
        },
        reponse: ["tapioca"],
      },
      {
        user_id: {
          $oid: "b6b70539-99c5-49db-bdc2-7b1435ffcc6b",
        },
        reponse: ["chasuble", "tapioca", "verve"],
      },
      {
        user_id: {
          $oid: "111f3772-912b-4c6d-b714-0d17ec606f67",
        },
        reponse: ["chasuble"],
      },
      {
        user_id: {
          $oid: "579a4e5f-118a-4b0a-8f4b-491fde29fe2d",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "6ea85a3f-7754-46f4-b824-4c70d9489d3f",
        },
        reponse: ["tapioca"],
      },
      {
        user_id: {
          $oid: "e255a04c-f8f5-4b01-abae-13479342905c",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "a4ef0bf3-aaf4-48fd-a028-963b29107b1a",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "6ea85a3f-7754-46f4-b824-4c70d9489d3f",
        },
        reponse: ["accelerator", "verve", "chasuble", "tapioca"],
      },
      {
        user_id: {
          $oid: "579a4e5f-118a-4b0a-8f4b-491fde29fe2d",
        },
        reponse: ["verve", "accelerator", "tapioca"],
      },
    ],
    results: [],
  },
  {
    id: "survey-014",
    creator: {
      user_id: {
        $oid: "1c136783-769f-460b-96bf-b7d7273266eb",
      },
    },
    question: "Adflicto uberrime utpote absens deputo teres valetudo alias.",
    description:
      "Bene arguo illo atqui armarium fugiat vulpes tergeo corpus. Peior aliqua alii tremo amissio amaritudo tepesco abeo tracto aeger. Decens statua inventore placeat.",
    date: {
      create: "2024-02-25",
      start: "2025-02-24",
      end: "2025-11-14",
      update: "2024-11-28",
    },
    choix: ["density", "academics", "cap", "waterspout"],
    reponses: [
      {
        user_id: {
          $oid: "fe885170-5f83-49e0-84d6-9363a456574a",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "b8c5b850-518d-4536-89c3-9e8a1526a8f5",
        },
        reponse: ["density", "cap"],
      },
      {
        user_id: {
          $oid: "9190cd21-d512-4164-bb19-68c4dbe38ae3",
        },
        reponse: ["academics", "waterspout"],
      },
      {
        user_id: {
          $oid: "e24541c2-8d86-4b2e-b631-73037fed61c3",
        },
        reponse: ["academics", "density", "waterspout"],
      },
      {
        user_id: {
          $oid: "493f80f7-3734-42b3-90bf-f51dfcf7ba15",
        },
        reponse: ["density", "waterspout", "cap", "academics"],
      },
      {
        user_id: {
          $oid: "8c9e3ed3-e858-4132-99d3-72b7dfe41bc7",
        },
        reponse: ["density", "academics"],
      },
      {
        user_id: {
          $oid: "ca51ebd2-0096-4698-ab4e-78026188be6a",
        },
        reponse: [],
      },
    ],
  },
  {
    creator: {
      user_id: {
        $oid: "c1b34415-5fab-4453-bcae-644161604e43",
      },
    },
    question:
      "Demergo aveho explicabo somnus cattus spiritus reiciendis suscipit.",
    description:
      "Amoveo cribro toties vulgivagus vomito vir arca. Defleo apto depulso quibusdam tero censura synagoga teneo callide. Cernuus optio torrens patruus cotidie eaque nemo canto dolore.",
    date: {
      create: "2024-01-17",
      start: "2025-09-18",
      end: "2024-12-28",
      update: "2024-11-28",
    },
    choix: ["brush", "hose", "barracks", "feather", "tentacle"],
    reponses: [
      {
        user_id: {
          $oid: "a2d8ff5b-add0-48de-afec-0b9bf187e260",
        },
        reponse: ["feather"],
      },
      {
        user_id: {
          $oid: "17d0642e-0af9-48af-a441-fabb709813d7",
        },
        reponse: ["brush", "barracks"],
      },
      {
        user_id: {
          $oid: "d4edb873-2ae7-4daf-8bf6-b11ed9e1cd32",
        },
        reponse: ["hose", "tentacle"],
      },
      {
        user_id: {
          $oid: "b05baf69-7ee3-4995-9095-dd61b0f7af05",
        },
        reponse: ["tentacle"],
      },
      {
        user_id: {
          $oid: "5ffbf263-fd57-4933-ae11-5903a81410ae",
        },
        reponse: ["feather", "brush", "tentacle", "barracks", "hose"],
      },
      {
        user_id: {
          $oid: "7e1932f4-f717-4024-aa09-8d48f47ed68e",
        },
        reponse: ["brush", "tentacle", "hose", "feather", "barracks"],
      },
      {
        user_id: {
          $oid: "6fb68895-050a-4cfc-a25c-672a8861fe6f",
        },
        reponse: ["hose", "barracks", "tentacle"],
      },
    ],
  },
  {
    creator: {
      user_id: {
        $oid: "8a7994a8-bb97-4aef-9cf9-48853b5de62e",
      },
    },
    question: "Vulnus iste cornu toties damnatio tricesimus ducimus surgo.",
    description:
      "Totus consuasor defaeco vester sordeo bellum. Coruscus argentum audentia virtus. Laboriosam coaegresco aureus arca aequitas conor carbo.",
    date: {
      create: "2024-07-13",
      start: "2025-04-18",
      end: "2025-09-10",
      update: "2024-11-27",
    },
    choix: ["restaurant", "rule"],
    reponses: [
      {
        user_id: {
          $oid: "5edc5278-64d3-4b1f-a695-60c4ecaf2c9f",
        },
        reponse: ["rule", "restaurant"],
      },
    ],
  },
  {
    creator: {
      user_id: {
        $oid: "5edc5278-64d3-4b1f-a695-60c4ecaf2c9f",
      },
    },
    question: "Cruentus assentator dens vilitas cultura alii casus eaque.",
    description:
      "Ex vester textor agnitio vicissitudo dolore aptus. Tergo teneo vorago cattus perferendis vestigium vulgus impedit. Ater coruscus tantillus adeptio vulpes praesentium vergo adsidue.",
    date: {
      create: "2024-06-10",
      start: "2025-02-24",
      end: "2025-01-30",
      update: "2024-11-27",
    },
    choix: ["championship", "gown", "appliance"],
    reponses: [
      {
        user_id: {
          $oid: "1f03ea31-1f3b-4af7-8e54-f18e2a5beab8",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "73fb90ba-7a6d-44ea-bdeb-261d625635f1",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "38e7d99f-65fc-4d87-9f8d-530554beef0b",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "d3e11ab8-2fcd-4e43-9de3-03d55118ffdb",
        },
        reponse: ["gown"],
      },
      {
        user_id: {
          $oid: "65ff16f5-ab8c-4dbe-8a28-c5b803103d9d",
        },
        reponse: [],
      },
      {
        user_id: {
          $oid: "b746895a-ee0e-47c1-93ae-4cf979b5ee52",
        },
        reponse: ["gown", "championship", "appliance"],
      },
      {
        user_id: {
          $oid: "38e7d99f-65fc-4d87-9f8d-530554beef0b",
        },
        reponse: ["gown", "appliance", "championship"],
      },
      {
        user_id: {
          $oid: "f1cbb17b-6584-49e8-822c-602a4b7cd530",
        },
        reponse: ["championship"],
      },
    ],
  },
]);

db = db.getSiblingDB("test");

db.test.drop();
