<template>
    <v-content>
        <v-container
                class="fill-height"
                fluid
        >
            <v-row
                    align="center"
                    justify="center"
            >
                <v-col
                        cols="12"
                        sm="8"
                        md="4"
                >
                    <v-card class="elevation-12">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Login form</v-toolbar-title>
                            <v-spacer/>
                        </v-toolbar>
                        <v-card-text>
                            <b-nav-form @submit.prevent="login" v-if="token==null">
                                <b-form-input id="username" size="sm" class="mr-sm-2" v-model="username"
                                              placeholder="username"
                                              name="username"></b-form-input>
                                <b-form-input id="password" size="sm" class="mr-sm-2" placeholder="password"
                                              type="password"
                                              v-model="password" name="password"></b-form-input>
                            </b-nav-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer/>
                            <v-btn color="primary" v-on:click="login">Login</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';
    import {TokenService} from "../storage/service";
    import router from "../router";

    export default {
        name: "login",
        data: function () {
            return {
                token: null,
                username: '',
                password: '',

            }
        },
        methods: {
            login: function () {
                axios.post('http://127.0.0.1:8000/auth/', {
                    username: this.username,
                    password: this.password,
                }).then(resp => {

                    this.token = resp.data.token;
                    console.log(this.token);
                    localStorage.setItem('user-token', resp.data.token);
                    router.push({ path: '/' })
                }).catch(err => {
                    localStorage.removeItem('user-token');
                    console.log(err);
                })
            },
        },
        created: function () {
            this.token = TokenService.getToken() || null;
            console.log("token:", this.token);

        }

    }
</script>

<style scoped>

</style>