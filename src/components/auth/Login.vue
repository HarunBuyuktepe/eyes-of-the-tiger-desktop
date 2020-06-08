<template>
<v-container fluid fill-height style="background: #F3E7E5">
    
        <v-row justify="center" align="center">
        <v-card style="width:400px" elevation="10"> 
            <v-card-title class="pa-2"> 
                <v-row justify="center">Select Username </v-row>
            </v-card-title>
            <v-list width="400" class="pa-1">
          <v-list-item v-for="user in users" :key="user" @click="clickUsername(user)" color="primary">
            <v-list-item-content>
              <v-list-item-title> 
                <v-row justify="center">
                  {{user}}
                </v-row>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-btn
                color="pink"
                dark
                small
                absolute
                bottom
                right=""
                fab
                @click="dialog=true"
              >
              <v-icon>mdi-plus</v-icon>
              </v-btn>
        </v-card>
        </v-row>

<v-dialog
      v-model="dialog"
      width="500"
    >
      <v-card>
        <v-card-title
          class="body-2"
          primary-title
        >
          Create User
        </v-card-title>

        <v-divider></v-divider>
        <v-row justify="center" align="center">
            <v-col cols="4">
                Username: 
            </v-col>
            <v-col cols="4">
               <v-text-field v-model="UserName"/> 
            </v-col>
        </v-row>
       
               <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="calibrate()"
            class="body-2"
          >
            Go to Calibration
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
        
    </v-container>
</template>

<script>
    export default {
        name: "Login",
        created() {
            this.getUsers()
        },
        data() {
            return {
                users: null,
                dialog: false,
                UserName: null
            }
        },
        methods: {
            getUsers(){
                this.$http.get('http://localhost:9099/get_users').then((response) => {
                        console.log(response.data)
                        this.users = response.data

                    })
            },
            clickUsername(user){
                console.log(user)
                this.$store.state.user = user
                this.$router.push({name: "Home", params: {username: user}})
            },
            calibrate(){
                 this.$http.get('http://localhost:9099/calibrate/'.concat(this.UserName)).then((response) => {
                        console.log(response.data)
                        if(response.data.message==="success"){
                            this.$store.state.user = this.UserName
                            this.$router.push({name: "Home",params: {username: this.UserName}})
                        }
                        this.dialog= false

                    })
                
            }
        }
    }
</script>

