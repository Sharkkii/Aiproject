<template>
  <div id="v-rl-panel">
    <div class="sub-header">
      <p>RL Panel</p>
    </div>
    <div class="window">
      <div class="indices">
        <div class="index">
          <button
            name="train"
            v-on:click="toggle('train')"
            v-bind:checked="checked.train"
          >
            Train Model
          </button>
        </div>
        <div class="index">
          <button
            name="usePretrained"
            v-on:click="toggle('usePretrained')"
            v-bind:checked="checked.usePretrained"
          >
            Use Pretrained Model
          </button>
        </div>
      </div>
      <div class="tab train" v-show="checked.train">
        <v-model-init-button v-on:initialize-model="initializeModel">
        </v-model-init-button>
      </div>
      <div class="tab use-pretrained" v-show="checked.usePretrained">
        <v-model-load-button v-on:load-model="loadModel">
        </v-model-load-button>
      </div>
      <v-model-train-button v-on:train-model="trainModel" v-bind:status="status.train">
        </v-model-train-button>
        <v-model-save-button v-on:save-model="saveModel" v-bind:status="status.save">
        </v-model-save-button>
    </div>
  </div>
</template>

<style scoped lang="scss">
#v-rl-panel {
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

.indices {
  display: flex;
}

.index {
  width: 50%;

  button {
    box-sizing: border-box;
    font-size: 20px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    width: 100%;
    &[checked] {
      border-width: medium;
      font-weight: bold;
    }
  }
}
</style>

<script>
import VModelInitButton from "../molecules/VModelInitButton.vue"
import VModelTrainButton from "../molecules/VModelTrainButton.vue"
import VModelLoadButton from "../molecules/VModelLoadButton.vue"
import VModelSaveButton from "../molecules/VModelSaveButton.vue"
export default {
  name: "VRlPanel",
  components: {
    VModelInitButton,
    VModelTrainButton,
    VModelLoadButton,
    VModelSaveButton
  },
  data: function() {
    return {
      checked: {
        train: true,
        usePretrained: false
      }
    }
  },
  props: {
    status: {
      type: Object,
      default: function() {
        return {
          train: "NG",
          save: "NG"
        }
      }
    }
  },
  methods: {
    toggle: function(name) {
      let self = this;
      if (this.checked.hasOwnProperty(name)) {
        Object.keys(self.checked).forEach(function(key) {
          if (key === name) {
            self.checked[key] = true;
          } else {
            self.checked[key] = false;
          }
        })
      }
    },
    initializeModel: function(data) {
      this.$emit("initialize-model", data);
    },
    trainModel: function(data) {
      this.$emit("train-model", data);
    },
    saveModel: function(data) {
      this.$emit("save-model", data);
    },
    loadModel: function(data) {
      this.$emit("load-model", data);
    }
  }
}
</script>