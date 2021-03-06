<template>
<div>
  <div id="v-dashboard">
    <div class="float-left">
      <div class="v-task-panel">
        <v-task-panel
          v-bind:reference-task-list="referenceTaskList"
          v-on:create-task="createTask"
          v-on:delete-reference-task="deleteReferenceTask"
          v-on:create-reference-task="createReferenceTask"
        >
        </v-task-panel>
      </div>
      <div class="v-schedule-panel">
        <v-schedule-panel
          v-on:get-best-schedule="getBestSchedule"
        >
        </v-schedule-panel>
      </div>
      <div class="v-rl-panel">
        <v-rl-panel
          v-on:initialize-model="initializeModel"
          v-on:train-model="trainModel"
          v-on:save-model="saveModel"
          v-on:load-model="loadModel"
          v-bind:status="status"
        >
        </v-rl-panel>
      </div>
    </div>
    <div class="float-left">
      <div class="v-task-monitor">
        <v-task-monitor v-bind:task-list="taskList" v-on:delete-task="deleteTask"></v-task-monitor>
      </div>
      <div class="v-schedule-monitor">
        <v-schedule-monitor
          v-bind:schedule-list-property="scheduleList"
          v-bind:n-slot="modelConfiguration.nSlot"
          v-bind:n-worker="modelConfiguration.nWorker"
        >
        </v-schedule-monitor>
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
      scheduleList: [],
      modelInformation: {},
      modelConfiguration: {},
      modelScore: {},
      status: {
        train: "NG",
        save: "NG"
      }
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
    deleteReferenceTask: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("delete-reference-task", data)
      .then(function(response) {
        self.getReferenceTaskList()
      })
    },
    getBestSchedule: function(data) {
      let self = this
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("get-best-schedule", data)
      .then(function(response) {
        
        let _nSlot = self.modelConfiguration.nSlot
        let _nWorker = self.modelConfiguration.nWorker
        let decode = function(x, base, order) {
          let _x = x
          let y = new Set()
          for (let i=0; i<order; i++) {
            y.add(_x % base)
            _x = Math.floor(_x / base)
          }
          return Array.from(y)
        }

        let _scheduleList = Object.values(response.data)
        _scheduleList = _scheduleList.map(function(_schedule) {
          return Object.values(_schedule).map(function(_action) {
            return decode(_action, _nSlot, _nWorker)
          })
        })
        self.scheduleList = _scheduleList

      })
    },
    initializeModel: function(data) {
      let self = this
      self.status = {
        train: "NG",
        save: "NG"
      }
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("initialize-model", data)
      .then(function(response) {
        
        let oldModelInformation = Object.assign({}, self.modelInformation)
        let oldModelConfiguration = Object.assign({}, self.modelConfiguration)

        let newModelInformation = Object.assign(oldModelInformation, {
          envName: response.data["env_name"],
          agentName: response.data["agent_name"],
          agentStatus: response.data["agent_status"]
        })
        let newModelConfiguration = Object.assign(oldModelConfiguration, {
          nSlot: response.data["n_slot"],
          nWorker: response.data["n_worker"]
        })

        self.modelInformation = newModelInformation
        self.modelConfiguration = newModelConfiguration

        self.status = {
          train: "OK",
          save: "OK"
        }
        console.log("initialize-model", response.data["status"])

      })
    },
    trainModel: function(data) {
      let self = this
      self.status = {
        train: "NG",
        save: "NG"
      }

      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("train-model", data)
      .then(function(response) {

        let oldModelInformation = Object.assign({}, self.modelInformation)
        let oldModelConfiguration = Object.assign({}, self.modelConfiguration)
        let oldModelScore = Object.assign({}, self.modelScore)

        let newModelInformation = Object.assign(oldModelInformation, {
          envName: response.data["env_name"],
          agentName: response.data["agent_name"],
          agentStatus: response.data["agent_status"]
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

        self.status = {
          train: "OK",
          save: "OK"
        }
        console.log("train-model", response.data["status"])
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
          agentName: response.data["agent_name"],
          agentStatus: response.data["agent_status"]
        })
        self.modelInformation = newData

        console.log("save-model", response.data["status"])
      })
    },
    loadModel: function(data) {
      let self = this
      self.status = {
        train: "NG",
        save: "NG"
      }
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios
      .post("load-model", data)
      .then(function(response) {

        let oldModelInformation = Object.assign({}, self.modelInformation)
        let oldModelConfiguration = Object.assign({}, self.modelConfiguration)

        let newModelInformation = Object.assign(oldModelInformation, {
          envName: response.data["env_name"],
          agentName: response.data["agent_name"],
          agentStatus: response.data["agent_status"]
        })
        let newModelConfiguration = Object.assign(oldModelConfiguration, {
          nSlot: response.data["n_slot"],
          nWorker: response.data["n_worker"]
        })

        self.modelInformation = newModelInformation
        self.modelConfiguration = newModelConfiguration

        self.status = {
          train: "OK",
          save: "NG"
        }
        console.log("load-model", response.data["status"])
      })
    }
  },
  mounted: function() {
    this.getTaskList()
    this.getReferenceTaskList()
  }
}
</script>