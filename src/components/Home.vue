<template>
    <v-container fluid>
        <v-row align="center" justify="center">
            <v-img height="300" width="500" background-position="background-position: center;" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKU_pV5oCFMnPMH6rpDKcqpc5kCxJSkTJUxxqTvJZvXwT16NPu&s" aspect-ratio="1.7" max-width="500" max-height="300"  contain></v-img>

        </v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleCreateButton()">Start</v-btn>
        </v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleCreateButton()">Settings</v-btn>
        </v-row>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-btn width="250" height="50" rounded color="primary" dark @click="handleCreateButton()">Tiger Team</v-btn>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {}
        },
        methods: {}
    }
</script>

