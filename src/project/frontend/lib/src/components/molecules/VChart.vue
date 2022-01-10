<template>
<div id="v-chart">
  <canvas id="cover-miss-rate-chart"></canvas>
  <!-- <canvas id="reward-chart"></canvas> -->
  <form method="GET" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <label>
          <p>Experiment</p>
          <div><input type="text" v-model="experimentName"></div>
        </label>
      </div>
      <div class="item">
        <button type="submit">
          <p>Load</p>
        </button>
      </div>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
#v-chart {

  .items {
    display: flex;
    align-items: flex-end;
    height: 100px;
  }

  .item {

    width: 50%;

    input {
      box-sizing: border-box;
      font-size: 20px;
      height: 50px;
      width: 100%;
    }

    button {
      box-sizing: border-box;
      font-size: 20px;
      height: 50px;
      width: 100%;
    }
  }

}
</style>

<script>
const axios = require("axios")
import Chart from "chart.js"
export default {
  name: "VChart",
  data: function() {
    return {
      coverMissRateChart: null,
      coverRate: [],
      missRate: [],
      experimentName: ""
    }
  },
  props: {
    coverRateProperty: {
      type: Array,
      default: function() {
        return []
      }
    },
    missRateProperty: {
      type: Array,
      default: function() {
        return []
      }
    }
  },
  methods: {
    submit: function() {
      this.getExperimentalResult({
        name: this.experimentName
      })
    },
    getExperimentalResult: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .get("get-experimental-result", {
        params: {
          name: data.name
        }
      })
      .then(function(response) {
        self.coverRate = response.data["covered"]
        self.missRate = response.data["missed"]
        self.renderChart()
      })
    },
    getData: function(data) {
      return data
    },
    getLabels: function(data) {
      let n = data.length
      let labels = new Array(n)
      for (let i=0; i<n; i++) { labels[i] = i.toString() }
      return labels;
    },
    renderCoverMissRateChart: function() {

      if (this.coverMissRateChart) {
        this.coverMissRateChart.destroy()
      }

      // data & labels
      let coverRateData = this.getData(this.coverRate)
      let missRateData = this.getData(this.missRate)
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
            x: {
              ticks: {
                display: false
              }
            },
            y: {
              ticks: {
                min: 0, max: 1
              }
            }
          }
        }
      }

      // chart
      const coverMissRateContext = document.getElementById("cover-miss-rate-chart")
      this.coverMissRateChart = new Chart(
        coverMissRateContext,
        config
      )

    },
    renderChart: function() {
      this.renderCoverMissRateChart()
    }
  },
  watch: {
    coverRateProperty: function() {
      this.coverRate = this.coverRateProperty
      this.renderChart()
    },
    missRateProperty: function() {
      this.missRate = this.missRateProperty
      this.renderChart()
    }
  },
  mounted: function() {
    this.renderChart()
  }
}
</script>