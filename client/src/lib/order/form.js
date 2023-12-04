import { EmailInputValidator } from "$lib/share/form/email-input.svelte";
import { FormField, FormGroup } from "$lib/share/form/form";
import { TextInputValidator } from "$lib/share/form/text-input.svelte";

export class AddressFormGroup extends FormGroup {
    constructor() {
        super();
        this.fullName = new FormField('', TextInputValidator.checkRequired('Full name is required'));
        this.email = new FormField(
            '',
            EmailInputValidator.checkRequired('Email is required'),
            EmailInputValidator.checkFormat('Incorrect email. Example: bob@test.com')
        );
        this.phoneNumber = new FormField('', TextInputValidator.checkRequired("Phone number is required"));
        this.address = new FormField('', TextInputValidator.checkRequired('Address is required'));
        this.address2 = new FormField(undefined);
    }
}

export class OrderFormGroup extends FormGroup {
    constructor() {
        super();
        this.billingAddress = new AddressFormGroup();
        this.shippingAddress = null;
    }
}