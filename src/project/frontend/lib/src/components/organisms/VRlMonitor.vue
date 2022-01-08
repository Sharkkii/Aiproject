<template>
<div id="v-rl-monitor">
  <div class="sub-header">
    <p>RL Monitor</p>
  </div>
  <div class="chart">
    <v-chart v-bind:covered="modelScore.covered" v-bind:missed="modelScore.missed">
    </v-chart>
  </div>
  <div class="table">
    <table>
      <tr>
        <td>env_name</td>
        <td>{{ this.envName }}</td>
      </tr>
      <tr>
        <td>agent_name</td>
        <td>{{ this.agentName }}</td>
      </tr>
      <tr>
        <td>n_slot</td>
        <td>{{ modelConfiguration.nSlot }}</td>
      </tr>
      <tr>
        <td>n_worker</td>
        <td>{{ modelConfiguration.nWorker }}</td>
      </tr>
      <tr>
        <td>n_epoch</td>
        <td>{{ modelConfiguration.nEpoch }}</td>
      </tr>
      <tr>
        <td>n_train_eval</td>
        <td>{{ modelConfiguration.nTrainEval }}</td>
      </tr>
      <tr>
        <td>n_test_eval</td>
        <td>{{ modelConfiguration.nTestEval }}</td>
      </tr>
    </table>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-rl-monitor {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  padding: 20px;
  width: 600px;
}

.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}

td {
  font-size: 20px;
  height: 50px;
  line-height: 50px;
  width: 200px;

  &:first-child {
    font-weight: bold;
  }

  &:second-child {
    font-weight: normal;
  }
}
</style>

<script>
import VChart from "../molecules/VChart.vue"
export default {
  name: "VRlMonitor",
  props: {
    modelInformation: {
      type: Object,
      default: function() {
        return {}
      }
    },
    modelConfiguration: {
      type: Object,
      default: function() {
        return {}
      }
    },
    modelScore: {
      type: Object,
      default: function() {
        return {}
      }
    }
  },
  computed: {
    envName: function() {
      return this.modelInformation.envName
    },
    agentName: function() {
      let name = this.modelInformation.agentName
      let status = this.modelInformation.agentStatus
      if (name) {
        return `${name} (${status})`
      } else {
        return ""
      }
    }
  },
  components: {
    VChart
  }
}
</script>