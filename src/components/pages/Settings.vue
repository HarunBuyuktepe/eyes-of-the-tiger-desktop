<template>
  <v-container fluid fill-height>
    <img src="../../assets/White-Tiger-Face-HD-1920x1080.jpg" style="position: fixed; " />
    <v-row align="center" justify="center">
      <v-col>
        <v-card class="mx-auto" max-width="400" style="opacity: 0.92">
          <v-card-title>Settings</v-card-title>
          <v-row class="ma-2" justify="center">
            <v-col cols="9" class="pa-2">
              <v-text-field
                v-model="size1"
                label="Move Per Frame"
                append-icon="info"
                @click:append="sizeOne()"
              />
            </v-col>
          </v-row>
          <v-row class="ma-2" justify="center">
            <v-col cols="9" class="pa-2">
              <v-text-field
                v-model="size2"
                label="Frame Number For Train"
                append-icon="info"
                @click:append="sizeTwo()"
              />
            </v-col>
          </v-row>
          <v-row class="ma-2" justify="center">
            <v-col cols="9" class="pa-2">
              <v-text-field
                v-model="size3"
                label="Scroll Up/Down Threshold"
                append-icon="info"
                @click:append="sizeThree()"
              />
            </v-col>
          </v-row>
          <v-card-actions>
            <v-row justify="center">
              <v-btn text dark color="pink" @click="goHome()">Retun Home Page</v-btn>
            </v-row>
            <v-row justify="center">
              <v-btn text dark color="pink" @click="saveSettings()">Save And Calibrate</v-btn>
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
          <v-spacer />
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
    console.log("Setting Page");
    this.user = this.$store.state.user;
    console.log(this.$store.state.user);
    console.log(this.$route.params.username);
    this.$http
      .get("http://localhost:9099/get_user_settings/".concat(this.user))
      .then(response => {
        console.log(response.data);
        this.size1 = response.data.MovePerFrame;
        this.size2 = response.data.FrameNumberForTrain;
        this.size3 = response.data.ScrollUpDownThreshold;
      });
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
    };
  },
  methods: {
    goHome() {
      this.$router.push({ name: "Home", params: { username: this.user } });
    },
    sizeOne() {
      this.dialog = true;
      this.currentTitle = "Move Per Frame";
      this.content =
        "Optimal value of the move per frame is 3. This settings directly change mouse movement.";
    },
    sizeTwo() {
      this.dialog = true;
      this.currentTitle = "Frame Number For Train";
      this.content =
        "Optimal value of the train frame number is 45. Increasing of number will take more time than before.";
    },
    sizeThree() {
      this.dialog = true;
      this.currentTitle = "Scroll Up/Down Threshold";
      this.content = "Optimal value of the Up/Down threshold is 50.";
    },
    saveSettings() {
      this.$http
        .post("http://localhost:9099/set_user_settings/".concat(this.user), {
          MovePerFrame: this.size1,
          FrameNumberForTrain: this.size2,
          ScrollUpDownThreshold: this.size3
        })
        .then(response => {
          console.log(response.data);
          this.size1 = response.data.MovePerFrame;
          this.size2 = response.data.FrameNumberForTrain;
          this.size3 = response.data.ScrollUpDownThreshold;
        });

      // this.$http
      // 	.get("http://localhost:9099/calibrate/".concat(this.user))
      // 	.then((response) => {
      // 		console.log(response.data);
      // 		if (response.data.message === "success") {
      // 			this.$store.state.user = this.UserName;
      // 			this.$router.push({
      // 				name: "Home",
      // 				params: { username: this.UserName },
      // 			});
      // 		}
      // 		this.dialog = false;
      // 	});
    }
  }
};
</script>
