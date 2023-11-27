export class TextFieldValidation {
    constructor() {
        /** @type {boolean} */
        this.dirty = false;
        /** @type {boolean} */
        this.valid = false;
        /** @type {string} */
        this.value = '';
        /** @type {string} */
        this.validationMessage = '';
        /** @type {string} */
        this.successMessage = '';
        /** @type {Validation[]} */
        this.validation = []
    }
}