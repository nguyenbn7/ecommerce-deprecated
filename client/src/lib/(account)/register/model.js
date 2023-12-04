import { FormField, FormGroup } from "$lib/share/form/class";
import { Validators } from "$lib/share/form/validation";

export class RegisterForm extends FormGroup {
    /**
     * @param {number | undefined} displayNameMaxLen
     */
    constructor(displayNameMaxLen) {
        super();
        this.displayName = new FormField(
            Validators.checkRequired('Name is required'),
            Validators.containsAlnumAndSpace('Name contains only letters and spaces'),
            Validators.checkMaxLength(`Name's max length is ${displayNameMaxLen} characters`, displayNameMaxLen)
        );

        this.email = new FormField(
            Validators.checkRequired('Email is required'),
            Validators.checkEmailFormat('Incorrect email. Example: bob@test.com')
        );

        this.password = new FormField(
            Validators.checkRequired('Password is required')
        );

        this.confirmPassword = new FormField(
            Validators.checkRequired('Confirm Password is required')
        );
    }
}