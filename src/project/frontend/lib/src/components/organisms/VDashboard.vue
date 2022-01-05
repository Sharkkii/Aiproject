<template>
<div>
  <div id="v-dashboard">
    <div class="float-left">
      <div class="v-task-panel">
        <v-task-panel v-on:create-task="createTask"  v-on:create-reference-task="createReferenceTask" v-bind:reference-task-list="referenceTaskList"></v-task-panel>
      </div>
      <div class="v-schedule-panel">
        <v-schedule-panel v-on:schedule-job="scheduleJob">
        </v-schedule-panel>
      </div>
      <div class="v-rl-panel">
        <v-rl-panel></v-rl-panel>
      </div>
    </div>
    <div class="float-left">
      <div class="v-task-monitor">
        <v-task-monitor v-bind:task-list="taskList" v-on:delete-task="deleteTask"></v-task-monitor>
      </div>
      <div class="v-schedule-monitor">
        <v-schedule-monitor v-bind:schedule-list="scheduleList"></v-schedule-monitor>
      </div>
      <div class="v-rl-monitor">
        <v-rl-monitor></v-rl-monitor>
      </div>
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

.v-task-panel {
  margin: 10px;
}

.v-task-monitor {
  margin: 10px;
}

.v-schedule-panel {
  margin: 10px;
}

.v-schedule-monitor {
  margin: 10px;
}

.v-rl-panel {
  margin: 10px;
}

.v-rl-monitor {
  margin: 10px;
}

.float-left {
  float: left;
}
</style>

<script>
import VScheduleButton from '../molecules/VScheduleButton.vue'
const axios = require("axios")
import VTaskPanel from "./VTaskPanel.vue"
import VTaskMonitor from "./VTaskMonitor.vue"
import VSchedulePanel from "./VSchedulePanel.vue"
import VScheduleMonitor from "./VScheduleMonitor.vue"
import VRlPanel from "./VRlPanel.vue"
import VRlMonitor from "./VRlMonitor.vue"
export default {
  name: "VDashboard",
  components: {
    VTaskPanel, VTaskMonitor, VSchedulePanel, VScheduleMonitor, VRlPanel, VRlMonitor, VScheduleButton
  },
  data: function() {
    return {
      taskList: [],
      referenceTaskList: [],
      scheduleList: {}
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
    getReferenceTaskList: function() {
      let self = this
      axios
      .get("get-reference-task-list")
      .then(function(response) {
        self.referenceTaskList = response.data
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
    },
    createReferenceTask: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("create-reference-task", data)
      .then(function(response) {
        self.getReferenceTaskList()
      })
    },
    deleteTask: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("delete-task", data)
      .then(function(response) {
        self.getTaskList()
      })
    },
    scheduleJob: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("schedule-job", data)
      .then(function(response) {
        self.scheduleList = response.data
      })
    }
  },
  mounted: function() {
    this.getTaskList()
    this.getReferenceTaskList()
  }
}
</script>