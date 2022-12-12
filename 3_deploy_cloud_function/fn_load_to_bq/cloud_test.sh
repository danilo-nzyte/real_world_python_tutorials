curl -X POST https://load-bq-data-psmosvfuya-nw.a.run.app \
   -H "Content-Type: application/json" \
   -d "{
        \"data\" : {
            \"dataset\": \"rick_and_morty\",
            \"table\": \"character\",
            \"results\": [{
    \"created\": \"Mon, 25 Oct 2021 09:18:48 GMT\",
    \"episode\": [
      \"https://rickandmortyapi.com/api/episode/49\"
    ],
    \"gender\": \"Female\",
    \"id\": 781,
    \"image\": \"https://rickandmortyapi.com/api/character/avatar/781.jpeg\",
    \"location\": {
      \"name\": \"Earth (Replacement Dimension)\",
      \"url\": \"https://rickandmortyapi.com/api/location/20\"
    },
    \"name\": \"Rick's Garage\",
    \"origin\": {
      \"name\": \"Earth (Replacement Dimension)\",
      \"url\": \"https://rickandmortyapi.com/api/location/20\"
    },
    \"species\": \"Robot\",
    \"status\": \"Alive\",
    \"type\": \"Artificial Intelligence\",
    \"url\": \"https://rickandmortyapi.com/api/character/781\"
  },
  {
    \"created\": \"Mon, 25 Oct 2021 09:20:57 GMT\",
    \"episode\": [
      \"https://rickandmortyapi.com/api/episode/49\"
    ],
    \"gender\": \"Male\",
    \"id\": 782,
    \"image\": \"https://rickandmortyapi.com/api/character/avatar/782.jpeg\",
    \"location\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"name\": \"Memory Squanchy\",
    \"origin\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"species\": \"Alien\",
    \"status\": \"Dead\",
    \"type\": \"Memory\",
    \"url\": \"https://rickandmortyapi.com/api/character/782\"
  },
  {
    \"created\": \"Mon, 25 Oct 2021 09:22:40 GMT\",
    \"episode\": [
      \"https://rickandmortyapi.com/api/episode/49\"
    ],
    \"gender\": \"Male\",
    \"id\": 783,
    \"image\": \"https://rickandmortyapi.com/api/character/avatar/783.jpeg\",
    \"location\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"name\": \"Memory Rick\",
    \"origin\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"species\": \"Human\",
    \"status\": \"Dead\",
    \"type\": \"Memory\",
    \"url\": \"https://rickandmortyapi.com/api/character/783\"
  },
  {
    \"created\": \"Mon, 25 Oct 2021 09:23:22 GMT\",
    \"episode\": [
      \"https://rickandmortyapi.com/api/episode/49\"
    ],
    \"gender\": \"Male\",
    \"id\": 784,
    \"image\": \"https://rickandmortyapi.com/api/character/avatar/784.jpeg\",
    \"location\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"name\": \"Memory Rick\",
    \"origin\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"species\": \"Human\",
    \"status\": \"Dead\",
    \"type\": \"Memory\",
    \"url\": \"https://rickandmortyapi.com/api/character/784\"
  },
  {
    \"created\": \"Mon, 25 Oct 2021 09:24:51 GMT\",
    \"episode\": [
      \"https://rickandmortyapi.com/api/episode/49\"
    ],
    \"gender\": \"Male\",
    \"id\": 785,
    \"image\": \"https://rickandmortyapi.com/api/character/avatar/785.jpeg\",
    \"location\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"name\": \"Memory Geardude\",
    \"origin\": {
      \"name\": \"Birdperson's Consciousness\",
      \"url\": \"https://rickandmortyapi.com/api/location/120\"
    },
    \"species\": \"Alien\",
    \"status\": \"Dead\",
    \"type\": \"Memory\",
    \"url\": \"https://rickandmortyapi.com/api/character/785\"
  }
]
        }
    }
"