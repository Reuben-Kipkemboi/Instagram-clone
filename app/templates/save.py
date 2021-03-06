<div class="container-fluid" id="register-page">
<div class="row">
    <div class="col-md-4"></div>
    <div class="col-md-4">
        <form class="shadow px-5" id="form" method="POST">
            {% csrf_token %}
            <h3 id="login-heading">Instagram</h3>
            <p class="text-center desc">Sign up to see photos and 
                <br>
                videos from your friends.</p>

            <button type="button" class="btn btn-primary btn-sm" id="facebook"><i class="fa-brands fa-facebook-square text-white"></i>Login with facebook</button>

            <p class="text-center p-3 font-weight-bold">OR</p>
            <div class="form-group">
                <label for="exampleInputEmail1">Mobile or Email</label>
                <label class="sr-only" for="inlineFormInputGroup"> email address</label>
                <div class="input-group mb-2">
                  <div class="input-group-prepend">
                    <div class="input-group-text"><i class="fa-solid fa-envelope fonts"></i>
                    </div></div>
                        
                  {{form.email}}
                </div>
            </div>
            <div class="form-group">
                <label for="exampleInputEmail1">Username</label>
                <label class="sr-only" for="inlineFormInputGroup">Full Name</label>
                <div class="input-group mb-2">
                  <div class="input-group-prepend">
                    <div class="input-group-text"><i class="fas fa-user fonts"></i></div>
                  </div>
                  {{form.username}}
                </div>
            </div>
            <div class="form-group">
                <label for="exampleInputEmail1">Password</label>
                <label class="sr-only" for="inlineFormInputGroup">Password</label>
                <div class="input-group mb-2">
                  <div class="input-group-prepend">
                    <div class="input-group-text"><i class="fa-solid fa-key fonts"></i></div>
                  </div>
                  {{form.password1}}
                </div>
            </div>
            <div class="form-group">
                <label for="exampleInputEmail1">Verify Password</label>
                <label class="sr-only" for="inlineFormInputGroup">Verify Password</label>
                <div class="input-group mb-2">
                  <div class="input-group-prepend">
                    <div class="input-group-text"><i class="fa-solid fa-key fonts"></i></div>
                  </div>
                  {{form.password2}}
                </div>
            </div>

            <button type="submit" class="btn p-2" id="register-btn">Sign Up</button>
            {{form.errors}}
        </form>
        <p class="text-center mt-2" id="login-redirect">
            <small class="font-weight-bold text-center">Already  have an Account? <a href="{% url 'login'%}">Log In</a></small>
        </p>
    </div>
    <div class="col-md-4"></div>
</div>
</div>