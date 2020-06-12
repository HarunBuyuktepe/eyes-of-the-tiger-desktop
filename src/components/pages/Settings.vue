<template>
  <v-container fluid fill-height>
    <img src="../../assets/White-Tiger-Face-HD-1920x1080.jpg"
         style="position: fixed; "/>
    <v-row align="center" justify="center">
      <v-col>
        <v-card
          class="mx-auto"
          max-width="400"
          style="opacity: 0.92"
        >
          <v-card-title>
            Settings
          </v-card-title>
          <v-row class="ma-2" justify="center">
            <v-col cols="9" class="pa-2">
              <v-text-field v-model="size1"
                            label="Move Per Frame"
                            append-icon="info"
                            @click:append="sizeOne()"/>
            </v-col>
          </v-row>
          <v-row class="ma-2" justify="center">
            <v-col cols="9" class="pa-2">
              <v-text-field v-model="size2"
                            label="Frame Number For Train"
                            append-icon="info"
                            @click:append="sizeTwo()"/>
            </v-col>
          </v-row>
          <v-row class="ma-2" justify="center">
            <v-col cols="9" class="pa-2">
              <v-text-field v-model="size3"
                            label="Scroll Up/Down Treshould"
                            append-icon="info"
                            @click:append="sizeThree()"/>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-row justify="center">
              <v-btn text dark color="pink" @click="goHome()">
                Retun Home Page
              </v-btn>
            </v-row>
            <v-row justify="center">
              <v-btn text dark color="pink">
                Save And Calibrate
              </v-btn>
            </v-row>
          </v-card-actions>

        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="dialog" max-width="360">
      <v-card>
        <v-card-title class="headline">{{ currentTitle }}</v-card-title>

        <v-card-text>{{ content }}</v-card-text>

        <v-card-actions>
          <v-spacer/>
          <v-btn text @click="dialog = false">Ok</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>


<script>

  export default {
    name: "Settings",
    created() {
      console.log("Setting Page")
      this.user =this.$store.state.user
      console.log(this.$store.state.user)
      console.log(this.$route.params.username)
    },
    data() {
      return {
        currentTitle: "",
        user: "",
        content: "",
        dialog: false,
        size1: "",
        size2: "",
        size3: ""
      }
    },
    methods: {
      goHome() {
this.$router.push({name: "Home", params: {username: this.user}})
      },
      sizeOne() {
        this.dialog = true;
        this.currentTitle = "Move Per Frame"
        this.content = ""
      },
      sizeTwo() {
        this.dialog = true;
        this.currentTitle = "Frame Number For Train"
        this.content = "denem"
      },
      sizeThree() {
        this.dialog = true;
        this.currentTitle = "Scroll Up/Down Treshould"
        this.content = "denem"
      },

    }
  }
</script>

