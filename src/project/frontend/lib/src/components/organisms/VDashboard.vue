<template>
<div>
  <div id="v-dashboard">
    <div class="float-left">
      <div class="v-control-panel">
        <v-control-panel v-on:create-task="createTask" v-bind:reference-task-list="referenceTaskList"></v-control-panel>
      </div>
      <div class="v-schedule-panel">
        <v-schedule-panel v-on:schedule-job="scheduleJob">
        </v-schedule-panel>
      </div>
    </div>
    <div class="float-left">
      <div class="v-view-monitor">
        <v-view-monitor v-bind:task-list="taskList"></v-view-monitor>
      </div>
      <div class="v-schedule-monitor">
        <v-schedule-monitor v-bind:schedule-list="scheduleList"></v-schedule-monitor>
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

.v-control-panel {
  margin: 10px;
}

.v-view-monitor {
  margin: 10px;
}

.v-schedule-panel {
  margin: 10px;
}

.v-schedule-monitor {
  margin: 10px;
}

.float-left {
  float: left;
}
</style>

<script>
import VScheduleButton from '../molecules/VScheduleButton.vue'
const axios = require("axios")
import VControlPanel from "./VControlPanel.vue"
import VViewMonitor from "./VViewMonitor.vue"
import VSchedulePanel from './VSchedulePanel.vue'
import VScheduleMonitor from './VScheduleMonitor.vue'
export default {
  name: "VDashboard",
  components: {
    VControlPanel, VViewMonitor, VSchedulePanel, VScheduleMonitor,
    VScheduleButton
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