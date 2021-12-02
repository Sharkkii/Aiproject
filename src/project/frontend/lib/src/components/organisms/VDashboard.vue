<template>
<div>
  <div id="v-dashboard">
    <div class="v-control-panel">
      <v-control-panel v-on:create-task="createTask"></v-control-panel>
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
const axios = require("axios")
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
  },
  methods: {
    getTaskList: function() {
      let self = this
      axios
      .get("get-task-list")
      .then(function(response) {
        self.taskList = response.data
      })
    },
    createTask: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("create-task", data)
      .then(function(response) {
        self.getTaskList()
      })
    }
  },
  mounted: function() {
    this.getTaskList()
  }
}
</script>