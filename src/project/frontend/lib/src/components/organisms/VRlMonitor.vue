<template>
<div id="v-rl-monitor">
  <div class="sub-header">
    <p>RL Monitor</p>
  </div>
  <div>
    <table>
      <tr>
        <td>model name</td>
        <td>{{ modelInformation.name }}</td>
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
  min-height: 400px;
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
  height: 40px;
  line-height: 40px;
  width: 160px;

  &:first-child {
    font-weight: bold;
  }
}
</style>

<script>
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
    }
  }
}
</script>