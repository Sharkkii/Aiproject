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
        <v-rl-panel
          v-on:initialize-model="initializeModel"
          v-on:setup-model="setupModel"
          v-on:train-model="trainModel"
          v-on:save-model="saveModel"
          v-on:load-model="loadModel"
        >
        </v-rl-panel>
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
        <v-rl-monitor v-bind:model-information="modelInformation" v-bind:model-configuration="modelConfiguration" v-bind:model-score="modelScore">
        </v-rl-monitor>
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
      scheduleList: {},
      modelInformation: {},
      modelConfiguration: {},
      modelScore: {}
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
    },
    initializeModel: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("initialize-model", data)
      .then(function(response) {
        let oldData = Object.assign({}, self.modelInformation)
        let newData = Object.assign(oldData, {
          modelName: response.data["model_name"],
          modelStatus: response.data["model_status"]
        })
        self.modelInformation = newData

        status = response.data["status"]
        console.log("initialize-model", status)
      })
    },
    setupModel: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("setup-model", data)
      .then(function(response) {
        let oldData = Object.assign({}, self.modelConfiguration)
        let newData = Object.assign(oldData, {
          nSlot: response.data["n_slot"],
          nWorker: response.data["n_worker"]
        })
        self.modelConfiguration = newData
      })
    },
    trainModel: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("train-model", data)
      .then(function(response) {

        let oldModelInformation = Object.assign({}, self.modelInformation)
        let oldModelConfiguration = Object.assign({}, self.modelConfiguration)
        let oldModelScore = Object.assign({}, self.modelScore)

        let newModelInformation = Object.assign(oldModelInformation, {
          modelName: response.data["model_name"],
          modelStatus: response.data["model_status"]
        })
        let newModelConfiguration = Object.assign(oldModelConfiguration, {
          nEpoch: response.data["n_epoch"],
          nTrainEval: response.data["n_train_eval"],
          nTestEval: response.data["n_test_eval"]
        })
        let newModelScore = Object.assign(oldModelScore, {
          covered: response.data["covered"],
          missed: response.data["missed"]
        })

        self.modelInformation = newModelInformation
        self.modelConfiguration = newModelConfiguration
        self.modelScore = newModelScore

        status = response.data["status"]
        console.log("train-model", status)
      })
    },
    saveModel: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("save-model", data)
      .then(function(response) {
        let oldData = Object.assign({}, self.modelInformation)
        let newData = Object.assign(oldData, {
          modelName: response.data["model_name"],
          modelStatus: response.data["model_status"]
        })
        self.modelInformation = newData

        status = response.data["status"]
        console.log("save-model", status)
      })
    },
    loadModel: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("load-model", data)
      .then(function(response) {
        let oldData = Object.assign({}, self.modelInformation)
        let newData = Object.assign(oldData, {
          modelName: response.data["model_name"],
          modelStatus: response.data["model_status"]
        })
        self.modelInformation = newData

        status = response.data["status"]
        console.log("load-model", status)
      })
    }
  },
  mounted: function() {
    this.getTaskList()
    this.getReferenceTaskList()
  }
}
</script>