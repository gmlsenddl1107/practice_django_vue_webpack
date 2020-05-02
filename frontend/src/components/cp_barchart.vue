<script>
    import {Bar} from 'vue-chartjs'

    export default {
        name: 'cp_barchart',
        extends: Bar,
        props: ['my_label','my_labels', 'my_datas'],
        data() {
            return {
                datacollection: {
                    labels: this.my_labels,
                    datasets: [
                        {
                            label: this.my_label,
                            backgroundColor: '#2B7A78',
                            pointBackgroundColor: 'white',
                            borderWidth: 1,
                            pointBorderColor: '#249EBF',
                            //Data to be represented on y-axis
                            data: this.my_datas
                        }
                    ]
                },
                //Chart.js options that controls the appearance of the chart
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                              min: 0,
                              max: 100,
                              stepSize: 20,
                            },
                            gridLines: {
                                display: true
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                display: false
                            }
                        }]
                    },
                    legend: {
                        display: true
                    },
                    responsive: true,
                    maintainAspectRatio: false
                }
            }
        },
        mounted() {
            //renderChart function renders the chart with the datacollection and options object.
            this.renderChart(this.datacollection, this.options)
        }
    }
</script>