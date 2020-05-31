<template>
    <v-container>
        <v-row>
            <v-col></v-col>
        </v-row>
        <v-row align="center" justify="center">
            <v-card
                    class="mx-auto"
                    max-width="800"
            >
                <div style="width: 800px"></div>
                <v-col>
                    <v-menu offset-y>
                        <template v-slot:activator="{ on }">
                            <v-btn style="background: darkslateblue"
                                   v-text="user"
                                   dark
                                   v-on="on"

                            >

                            </v-btn>
                        </template>
                        <v-list>
                            <v-list-tile
                                    v-for="(item, index) in items"
                                    :key="index"
                                    @click="user = item.title"
                            >
                                <v-row align="center" justify="center">
                                    <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                                </v-row>

                            </v-list-tile>
                        </v-list>
                    </v-menu>

                </v-col>
                <v-card-title>
                    A ayarı
                </v-card-title>

                <v-col>
                    <v-text-field v-model="size1"/>
                </v-col>

                <v-card-actions>


                    <v-spacer></v-spacer>

                    <v-btn
                            icon
                            @click="show1 = !show1"
                    >
                        <v-icon>{{ show1 ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                    </v-btn>
                </v-card-actions>

                <v-expand-transition>
                    <div v-show="show1">
                        <v-divider></v-divider>

                        <v-card-text>
                            şu ayardır optimali budur
                        </v-card-text>
                    </div>
                </v-expand-transition>

                <div style="width: 800px"></div>
                <v-card-title>
                    B ayarı
                </v-card-title>

                <v-col>
                    <v-text-field v-model="size2"/>
                </v-col>

                <v-card-actions>


                    <v-spacer></v-spacer>

                    <v-btn
                            icon
                            @click="show2 = !show2"
                    >
                        <v-icon>{{ show2 ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                    </v-btn>
                </v-card-actions>

                <v-expand-transition>
                    <div v-show="show2">
                        <v-divider></v-divider>

                        <v-card-text>
                            şu ayardır optimali budur
                        </v-card-text>
                    </div>
                </v-expand-transition>


                <div style="width: 800px"></div>
                <v-card-title>
                    C ayarı
                </v-card-title>

                <v-col>
                    <v-text-field v-model="size3"/>
                </v-col>

                <v-card-actions>


                    <v-spacer></v-spacer>

                    <v-btn
                            icon
                            @click="show3 = !show3"
                    >
                        <v-icon>{{ show3 ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                    </v-btn>
                </v-card-actions>

                <v-expand-transition>
                    <div v-show="show3">
                        <v-divider></v-divider>

                        <v-card-text>
                            şu ayardır optimali budur
                        </v-card-text>
                    </div>
                </v-expand-transition>
                <v-btn
                        color="purple"
                        text
                >
                    Save
                </v-btn>
            </v-card>
        </v-row>
    </v-container>
</template>


<script>

    export default {
        name: "Settings",
        created() {
            console.log("Setting Page")
            this.getUser();
        },
        data() {
            return {
                show1: false,
                size1: "3",
                show2: false,
                size2: "15",
                show3: false,
                size3: "2",
                user: "none",
                items: ""
            }
        },
        methods: {
            selectUser(item) {
                console.log(item)
                this.getUserProfile()
            },
            getUser() {
                // burada tüm user verilerini at diyecek
                // sonra tüm user verilerini dödürecek.
                // en üstte gelen aktif olacak
                console.log("get user")
                this.items = [
                    {title: 'Me'},
                    {title: 'User2'},
                    {title: 'User3'},
                    {title: 'User4'}
                ]
                this.selectUser(this.items[0].title)
            },
            getUserProfile() {
                console.log("Get User Profile")
                this.size1 = 5    ;
                this.size2 =  6  ;
                this.size3 =   12 ;

            }
        }
    }
</script>

