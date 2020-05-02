<template>

    <v-card class="elevation-3 ">
        <v-card color="light-green darken-3">
            <div class="overline  text-center"> {{ gpu_status.timestamp }}</div>
            <v-toolbar-title class="display-1 text-center">{{selected_server_name}}</v-toolbar-title>
        </v-card>
        <v-card class="pa-4" >
            <v-card-title>GPU Memory 사용량</v-card-title>
            <v-card  class="mx-10 grey lighten-2">
                <v-row   >
                    <div class="col text-center">
                        남은 gpu 메모리
                    </div>
                    <div class="col text-center">
                        사용 중인 gpu 메모리
                    </div>
                </v-row>
                <v-row>
                    <div class="col text-center">
                        {{gpu_status.memory_free}} MiB
                    </div>
                    <div class="col text-center">
                        {{gpu_status.memory_used}} MiB
                    </div>
                </v-row>
            </v-card>
            <p/>
            <p/>
            <v-row>
                <v-card-title>Utilzation of GPU</v-card-title>
            </v-row>
            <v-row class="px-10">
                <v-col>
                    <cp_barchart v-bind:my_labels="gpu_status.index_gpu"
                                 v-bind:my_datas="gpu_status.util_gpu"
                                 v-bind:my_label="gpu_status.label_gpu" name="gpu_status"
                                 style="min-height:150px;min-width:60px;"/>
                </v-col>
                <v-col>
                    <cp_barchart v-bind:my_labels="gpu_status.index_memory"
                                 v-bind:my_datas="gpu_status.util_memory"
                                 v-bind:my_label="gpu_status.label_memory" name="gpu_process"
                                 style="min-height:150px;min-width:60px"/>

                </v-col>
            </v-row>
            <v-row>
                <v-card-title>GPU Process</v-card-title>
            </v-row>
            <v-row class="px-10">
                <v-col>
                    <v-card class="align-center center" color="grey lighten-2">

                        <b-table class="text-center justify-content-center" hover :items="gpu_process" ></b-table>
                    </v-card>
                </v-col>

            </v-row>
        </v-card>
    </v-card>
</template>
<script>
    import cp_barchart from "./cp_barchart"

    export default {
        name: 'cp_gpu_process',
        props: ['selected_server_name'],
        components: {
            cp_barchart
        },
        data: () => ({
                gpu_status: {
                    utilzation_gpu: 947,
                    utilzation_memory: 2849,
                    timestamp: '2020-02-03 08:10:20',
                    memory_used: 234,
                    memory_free: 345,
                    label_gpu: 'gpu_util (%)',
                    index_gpu: ['gpu0', 'gpu1', 'gpu2', 'gpu3', 'gpu4', 'gpu5', 'gpu6', 'gpu7'],
                    util_gpu: [40, 39, 10, 40, 39, 80, 40, 10],
                    label_memory: 'gpu_memory_util (%)',
                    index_memory: ['gpu0', 'gpu1', 'gpu2', 'gpu3', 'gpu4', 'gpu5', 'gpu6', 'gpu7'],
                    util_memory: [40, 39, 10, 40, 39, 80, 50, 10]
                },
                gpu_process: [
                    {

                        gpu_uuid: 'atijalsdnfas',
                        gpu_index: 0,
                        pid: 19443,
                        used_gpu_memory: 193
                    },
                    {

                        gpu_uuid: 'atijalsdnfas',
                        gpu_index: 1,
                        pid: 19393,
                        used_gpu_memory: 193
                    },
                    {
                        gpu_uuid: 'atijalsdnfas',
                        gpu_index: 2,
                        pid: 1793,
                        used_gpu_memory: 193
                    }

                ],
            }
        )
    }
</script>
