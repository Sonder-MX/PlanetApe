import { Notify } from 'quasar'

/**
 * 参数说明
 * @nObj
 * {type: 'positive', message: '', position: 'top', timeout: 2000, color: 'white', textColor: 'black', icon: 'check_circle', actions: [{icon: 'close', color: 'white'}]
 */
export const nfy = (type, message, timeout = 2000, position = 'top', nObj) => {
  Notify.create({
    type,
    message,
    timeout,
    position,
    ...nObj,
  })
}
