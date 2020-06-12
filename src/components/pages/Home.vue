<template>
    <v-container fluid fill-height>
        <img src="../../assets/White-Tiger-Face-HD-1920x1080.jpg"
         style="position: fixed; "/>
       
        <v-row align="center" justify="center">
           <v-col cols="2">
               <v-row class="ma-3">
            <v-btn width="250" 
            height="50" 
            rounded color="primary" 
            dark 
            @click="handleStartButton()" 
            v-show="show">
                Start Button
            </v-btn>
            <v-btn width="250" 
            height="50" 
            rounded 
            color="primary" 
            dark 
            @click="handleStopButton()" v-show="!show">
                Stop Button
            </v-btn>
               </v-row>
            <v-row class="ma-3">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleSettingButton()">Settings</v-btn>
            </v-row>
            <v-row class="ma-3">
            <v-btn width="250" height="50" rounded color="primary" dark>Tiger Team</v-btn>
            </v-row>
            <v-row class="ma-3">
            <v-btn width="250" height="50" rounded color="primary" dark @click="goLogin()">Log Out</v-btn>
            </v-row>
           </v-col>
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
            goLogin() {
                this.$router.push({name: "Login"})
            },
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
                this.$router.push({name: "Settings",params: {username: this.user}})
            }
        }
    }
</script>

