import { Server, Room} from "colyseus"
import { MyRoom } from "./rooms/MyRoom.ts";

const port = parseInt(process.env.PORT, 10) || 8000


const gameServer = new Server()

gameServer.define('new_room', MyRoom)

gameServer.listen(port)
console.log(`[GameServer] Listenting on port: ${port}`)