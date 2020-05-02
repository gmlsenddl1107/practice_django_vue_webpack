<template>
    <v-container>
        <div class="row ">
            <v-toolbar color="grey lighten-2">

                <v-toolbar-title>
                    <p class="headline  font-weight-bold">현재 GPU 사용량</p>
                </v-toolbar-title>
                <v-toolbar-title>
                <p class="subtitle-2 ">    ( util_gpu : 1/6 ~ 1 second 사이의 GPU를 사용한 percentage )</p>


                </v-toolbar-title>
            </v-toolbar>
        </div>
        <br>
        <div class="row">
            <p class="headline  font-weight-bold">KDL Group</p>
        </div>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-md-4">
            <div v-for="item in gpu_status['KDL']" :key="item.server_name" class="col-md-3">

                <v-card class="pa-3">
                    <v-card-text>
                        <div>
                            {{ item.create_date}}
                        </div>
                        <p class="title text--primary">{{ item.server_name }}</p>
                    </v-card-text>
                    <div>
                        <cp_barchart :height="200" v-bind:my_labels="item.index_gpu"
                                     v-bind:my_datas="item.util_gpu"
                                     v-bind:my_label="item.label_gpu"/>

                    </div>
                    <v-card-actions>
                        <v-btn @click="showModal(item.server_name)">see more</v-btn>
                    </v-card-actions>
                </v-card>

            </div>
        </div>

        <div class="container">
            <div class="row">
                <p class="headline  font-weight-bold">KDL-S Group</p>
            </div>
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-md-4">
                <div v-for="item in gpu_status" :key="item.server_name" class="col-md-3">

                    <v-card class="pa-3">
                        <v-card-text>
                            <div>
                                {{ item.create_date}}
                            </div>
                            <p class="title text--primary">{{ item.server_name }}</p>
                        </v-card-text>
                        <div>
                            <cp_barchart :height="200" v-bind:my_labels="item.index_gpu"
                                         v-bind:my_datas="item.util_gpu"
                                         v-bind:my_label="item.label_gpu"/>

                        </div>
                        <v-card-actions>
                            <v-btn @click="showModal(item.server_name)">see more</v-btn>
                        </v-card-actions>
                    </v-card>

                </div>
            </div>
        </div>

        <v-dialog v-model="dialog">
            <cp_gpu_process v-bind:selected_server_name="selected_server_name"/>

        </v-dialog>
    </v-container>
</template>

<script>
    import cp_barchart from "./cp_barchart";
    import cp_gpu_process from "./cp_gpu_process"
    import {TokenService} from "../storage/service";
    import axios from "axios";

    export default {
        name: 'cp_gpu_status',

        components: {
            cp_barchart,
            cp_gpu_process

        },
        data: function () {
            return {
                dialog: false,
                gpu_status:'',
                selected_server_name: ""


            }
        },
        methods: {

            showModal(key) {
                this.selected_server_name = key
                this.dialog = true
                console.log(key)
            },

            getGpuStatus() {
                this.token = TokenService.getToken();
                console.log("token",this.token);
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    },
                };
                axios.get("http://127.0.0.1:8000/api/gpu/status/",axiosConfig)
                    .then(
                        res => (this.gpu_status = res.data)

                    )
                    .catch(err => console.log(err));
                console.log(this.gpu_status);
            }
        },
        created() {
            this.getGpuStatus();
        }

    }
</script>