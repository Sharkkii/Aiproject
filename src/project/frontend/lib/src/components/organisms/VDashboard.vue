<template>
<div>
  <div id="v-dashboard">
    <div class="v-control-panel">
      <v-control-panel></v-control-panel>
    </div>
    <div class="v-view-monitor">
      <v-view-monitor v-bind:task-list="taskList"></v-view-monitor>
    </div>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-dashboard {
  clear: both;
  display: flex;
  justify-content: center;
}

.v-control-panel {
  float: left;
  margin: 0 10px;
}

.v-view-monitor {
  float: left;
  margin: 0 10px;
}
</style>

<script>
import VControlPanel from "./VControlPanel.vue"
import VViewMonitor from "./VViewMonitor.vue"
export default {
  name: "VDashboard",
  components: {
    VControlPanel, VViewMonitor
  },
  data: function() {
    return {
      taskList: []
    }
  }
}
</script>