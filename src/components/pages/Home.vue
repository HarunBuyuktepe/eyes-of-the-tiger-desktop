<template>
    <v-container fluid>
        <v-row align="center" justify="center">
            <v-img height="300" width="500" background-position="background-position: center;"
                   src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKU_pV5oCFMnPMH6rpDKcqpc5kCxJSkTJUxxqTvJZvXwT16NPu&s"
                   aspect-ratio="1.7" max-width="500" max-height="300" contain></v-img>

        </v-row>
        <v-row justify="center">{{this.$store.state.user}}</v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleStartButton()" v-show="show">
                Start Button
            </v-btn>
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleStopButton()" v-show="!show">
                Stop Button
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
                show: "true",
                pid: "",
                user: this.$store.state.user
            }
        },
        methods: {
            handleStartButton() {
                    // eslint-disable-next-line no-undefined

                    this.$http.get("http://localhost:9099/start_without_calibration/".concat(this.user)).then((response) => {
                        
                        console.log(response.data)
                        this.pid = response.data.pid
                        console.log(this.pid)
                        this.show=false
                    })
            },
            handleStopButton() {
                    this.$http.get("http://localhost:9099/kill_program/".concat(this.pid)).then((response) => {
                        console.log(response)
                        this.show= true
                    })
                    
            },
            handleSettingButton() {
                this.$router.push({name: "settings", params: 'Settings'})
            }
        }
    }
</script>

