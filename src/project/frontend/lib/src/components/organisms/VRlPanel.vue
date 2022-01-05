<template>
<div id="v-rl-panel">
  <div class="sub-header">
    <p>RL Panel</p>
  </div>
  <div class="window">
    <div class="indices">
      <div class="index">
        <button name="train" v-on:click="toggle('train')" v-bind:checked="checked.train">
          Train Model
        </button>
      </div>
      <div class="index">
        <button name="test" v-on:click="toggle('test')" v-bind:checked="checked.test">
          Use Pretrained Model
        </button>
      </div>
    </div>
    <div class="tab train" v-if="checked.train">
      <v-model-init-button>
      </v-model-init-button>
      <v-model-setup-button>
      </v-model-setup-button>
      <v-model-train-button>
      </v-model-train-button>
      <v-model-save-button>
      </v-model-save-button>
    </div>
    <div class="tab test" v-if="checked.test">
      <v-model-load-button v-on:load-model="loadModel">
      </v-model-load-button>
    </div>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-rl-panel {
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
import VModelInitButton from '../molecules/VModelInitButton.vue'
import VModelSetupButton from '../molecules/VModelSetupButton.vue'
import VModelTrainButton from '../molecules/VModelTrainButton.vue'
import VModelLoadButton from '../molecules/VModelLoadButton.vue'
import VModelSaveButton from '../molecules/VModelSaveButton.vue'
export default {
  name: "VRlPanel",
  components: {
    VModelInitButton, VModelSetupButton, VModelTrainButton, VModelLoadButton, VModelSaveButton
  },
  data: function() {
    return {
      checked: {
        "train": true,
        "test": false
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
    loadModel: function(data) {
      this.$emit("load-model", data);
    }
  }
}
</script>