<template>
    <div class="">
        <div class="row">
            <div class="col-md-5 text-center nicefont">
                <h4>Welcome to Youtube Rater</h4>
                <v-btn @click="getVideos()"> submit
                </v-btn>

                <p v-bind:key="video.id" v-for="video in videos">
                    {{video.title}}
                    <br>
                    Rating: {{video.rating_average}}
                </p>
            </div>


        </div>

    </div>
</template>

<script>
    // @ is an alias to /src
    import axios from 'axios';
    import {TokenService} from "../storage/service";

    export default {
        name: 'home',
        components: {},
        data() {
            return {
                videos: [],
            }
        },
        methods: {
            getVideos() {
                this.token = TokenService.getToken();
                console.log("token",this.token);
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.get("http://127.0.0.1:8000/api/gpu/videos/",axiosConfig)
                    .then(res => (this.videos = res.data))
                    .catch(err => console.log(err));
            }
        },
    };
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Alatsi&display=swap');

    .nicefont {
        font-size: 26px;
        font-family: 'Alatsi', sans-serif;
    }
</style>