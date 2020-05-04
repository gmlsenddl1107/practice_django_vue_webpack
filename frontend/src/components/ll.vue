<template>
    <v-content>
        <v-container
                class="fill-height"
                fluid
        >
            <v-row

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
                            <v-form @submit.prevent="login" v-if="token==null">
                                <v-text-field  name="Username" label="Username" v-model="username"></v-text-field>
                                <v-text-field name="Password" label="Password" type="password" v-model="password">></v-text-field>
                                <v-card-actions>
                                    <v-btn primary large block v-on:click="login" >Login</v-btn>
                                </v-card-actions></v-form>
                            <v-alert v-if="message!=null" color="red">
                                {{message}}
                            </v-alert>
                        </v-card-text>
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
                message: null

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
                    this.message = err.toString();
                    console.log(err);
                })
            },
        },
        created: function () {
            this.token = TokenService.getToken() || null;


        }

    }
</script>

<style scoped>

</style>