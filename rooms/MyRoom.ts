import { Room } from "colyseus"

class MyRoom extends Room {
    maxClients = 4

    async onCreate(options) {
        console.log("Room created let's get it started!")
    }

    async onJoin(client, options) {
        console.log(`Client joined: ${client}`)
    }

    async onLeave(client, consented) {
        console.log(`Client left: ${client}`)
    }

    async onDispose() {
        console.log("Room has been disposed...")
    }
}