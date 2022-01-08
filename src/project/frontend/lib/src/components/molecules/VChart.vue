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
  data: function() {
    return {
      chart: null
    }
  },
  props: {
    covered: {
      type: Array,
      default: function() {
        return []
      }
    },
    missed: {
      type: Array,
      default: function() {
        return []
      }
    }
  },
  computed: {
    watched: function() {
      return this.covered, this.missed
    }
  },
  methods: {
    getData: function(data) {
      return data
    },
    getLabels: function(data) {
      let n = data.length
      let labels = new Array(n)
      for (let i=0; i<n; i++) { labels[i] = i.toString() }
      return labels;
    },
    renderChart: function() {

      if (this.chart) {
        this.chart.destroy()
      }

      // data & labels
      let coverRateData = this.getData(this.covered)
      let missRateData = this.getData(this.missed)
      let datasets = [
        {
          label: "covered",
          data: coverRateData,
          borderColor: "rgba(19, 170, 152, 0.5)",
          borderWidth: 5,
          fill: false,
          lineTension: 0,
        },
        {
          label: "missed",
          data: missRateData,
          borderColor: "rgba(205, 56, 75, 0.5)",
          borderWidth: 5,
          fill: false,
          lineTension: 0,
        }
      ]

      let labels = this.getLabels(coverRateData)
      let data = {
        labels: labels,
        datasets: datasets
      }

      // configurations
      const config = {
        type: "line",
        data: data,
        options: {
          scales: {
            xAxes: [{
              ticks: {
                display: false
              }
            }],
            yAxes: [{
              ticks: {
                min: 0, max: 1
              }
            }]
          }
        }
      }
      const ctx = document.getElementById("chart")

      // chart
      this.chart = new Chart(
        ctx,
        config
      )

    },
  },
  watch: {
    watched: function() {
      this.renderChart()
    }
  },
  mounted: function() {
    this.renderChart()
  }
}
</script>