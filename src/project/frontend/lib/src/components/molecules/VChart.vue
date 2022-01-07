<template>
<div id="v-chart">
  <canvas id="chart"></canvas>
</div>
</template>

<style scoped lang="scss">
#v-chart {
  canvas {
    height: 400px;
    width: 100%;
  }
}
</style>

<script>
import Chart from "chart.js"
export default {
  name: "VChart",
  methods: {
    renderChart: function() {

      // data & labels
      let labels = [ "1", "2", "3", "4" ]
      let data = {
        labels: labels,
        datasets: [{
          label: "data label",
          data: [ 1, 2, 3, 4 ]
        }]
      }

      // configurations
      const config = {
        type: "line",
        data: data,
        options: {}
      }
      const ctx = document.getElementById("chart")

      // chart
      let chart = new Chart(
        ctx,
        config
      )

    },
  },
  mounted: function() {
    this.renderChart()
  }
}
</script>