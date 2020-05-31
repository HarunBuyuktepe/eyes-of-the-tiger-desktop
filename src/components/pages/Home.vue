<template>
    <v-container fluid>
        <v-row align="center" justify="center">
            <v-img height="300" width="500" background-position="background-position: center;"
                   src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKU_pV5oCFMnPMH6rpDKcqpc5kCxJSkTJUxxqTvJZvXwT16NPu&s"
                   aspect-ratio="1.7" max-width="500" max-height="300" contain></v-img>

        </v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleStartStopButton()">
                {{buttonText}}
            </v-btn>
        </v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleSettingButton()">Settings</v-btn>
        </v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark>Tiger Team</v-btn>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "Home",
        created() {
        },
        data() {
            return {
                buttonText: "Start Program"
            }
        },
        methods: {
            handleStartStopButton() {
                if (this.buttonText === "Start Program") {
                    // eslint-disable-next-line no-undef
                    this.$http.get('http://localhost:8018/start_program').then((response) => {
                        console.log(response.data)
                    })

                    this.buttonText = "Stop Program"
                } else if (this.buttonText === "To Stop Press ESC and me") {
                    this.$http.get('http://localhost:8018/kill_program').then((response) => {
                        console.log(response.data)

                    })
                    this.buttonText = "Start Program"
                }
            },
            handleSettingButton() {
                this.$router.push({name: "settings", params: 'Settings'})
            }
        }
    }
</script>

