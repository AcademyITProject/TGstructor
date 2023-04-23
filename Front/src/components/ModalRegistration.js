import React, { Component } from 'react';
import axios from 'axios'

import loadIcon from './img/loading-svgrepo-com.svg'
import logo from './img/Vector.svg'
// import '../css/startPage.css'

import './css/modal.css'
class ModalRegistration extends Component {
    constructor(props) {
        super(props);
        this.state = {
          // showModal: false,
          name: '',
          email: '',
          password: '',
          confirmPassword: '',
          error: '',
          incor_name: false,
          incor_email: false,
          incor_pass: false,
          incor_onfPass: false
        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
      }
    
      handleInputChange = (event) => {
        const { name, value } = event.target;
        this.setState({ [name]: value });
      };
    
      handleSubmit = (event) => {
        event.preventDefault();
        // здесь можно добавить логику отправки формы на сервер
      };

      userRegistration = () => {
        if (this.state.name === ''){
          this.deleteError()
          this.setState({incor_name: true})
        }else if (this.state.email === ''){
          this.deleteError()
          this.setState({incor_email: true})
        }else if (this.state.password === ''){
          this.deleteError()
          this.setState({incor_pass: true})
        }else if (this.state.confirmPassword === ''){
          this.deleteError()
          this.setState({incor_confPass: true})
        }else if (this.state.confirmPassword !== this.state.password){
          this.deleteError()
          this.setState({error: 'Пороли не совпадают'})
        }else{
          this.setState({isLoaded: true});
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/login',
            data: {
              email: this.state.email,
              username: this.state.name,
              password: this.state.password
            }
          }).then((res) => {
            console.log(res)
            console.log('-----')
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/api/login',
              data: {
                email: res.data.email,
                password: res.data.password
              }
            }).then((res) => {
              console.log(res)
              console.log('-----')
              this.setState({
                isLoaded: false
              })
              this.props.onRegistration(res.data.email, res.data.password)
            })
          }).catch(err => {
            this.deleteError()
            this.setState({
              isLoaded: false,
              error: 'Данная почта уже зарегистрирована'
            })
            })
          }
      }

      
      deleteError = () => {
        this.setState({
          error: '',
          incor_pass: false,
          incor_email: false,
          incor_name: false,
          incor_confPass: false
        })
      }

      render() {
        const { onClose } = this.props;
        return (
            <div className={this.props.showModal ? "modal active" : "modal"} onClick={()=> 
              this.setState({
                error: '',
                incor_confPass: false,
                incor_email: false,
                incor_name: false,
                incor_pass: false
              }, this.props.onCloseModal())}>
            <div className={this.props.showModal ? "modal__content active" : "modal__content"} onClick={e=>e.stopPropagation()}>
              <img src={logo} className='size__logo'/>
              <h3 style={{paddingLeft:'40px'}}>Создайте аккаунт</h3>
              <form onSubmit={this.handleSubmit} className='input__form'>
                
                  
                  <input
                    type="text"
                    name="name"
                    placeholder='Имя'
                    value={this.state.name}
                    className='label'
                    onChange={this.handleInputChange}
                  />
                
                  <p className='text-4' 
                    style={{display: 'flex',width: '340px', height: '15px', margin: '0px', marginBottom: '5px', justifyContent: 'center', alignItems: 'center', color: 'red'}}>
                    {this.state.incor_name && 'Заполните поле'}
                  </p>
                  
                  <input
                    type="email"
                    name="email"
                    placeholder='Email'
                    className='label'
                    value={this.state.email}
                    onChange={this.handleInputChange}
                  />

                  <p className='text-4' 
                    style={{display: 'flex',width: '340px', height: '15px', margin: '0px', marginBottom: '5px', justifyContent: 'center', alignItems: 'center', color: 'red'}}>
                    {this.state.incor_email && 'Заполните поле'}
                  </p>
                  
                  <input
                    type="password"
                    name="password"
                    placeholder='Пароль'
                    className='label'
                    value={this.state.password}
                    onChange={this.handleInputChange}
                  />

                  <p className='text-4' 
                    style={{display: 'flex',width: '340px', height: '15px', margin: '0px', marginBottom: '5px', justifyContent: 'center', alignItems: 'center', color: 'red'}}>
                    {this.state.incor_password && 'Заполните поле'}
                  </p>
                  
                  <input
                    type="password"
                    name="confirmPassword"
                    className='label'
                    placeholder='Подтвердите пароль'
                    value={this.state.confirmPassword}
                    onChange={this.handleInputChange}
                  />

                  <p className='text-4' 
                    style={{display: 'flex',width: '340px', height: '15px', margin: '0px', marginBottom: '5px', justifyContent: 'center', alignItems: 'center', color: 'red'}}>
                    {this.state.incor_confPass && 'Заполните поле'}
                    {this.state.error}
                  </p>
                
                <button type="button" className='button text-2' style={{fontSize: '20px', width: '80%'}} onClick={() => this.userRegistration()}>Зарегестрироваться</button>
                <br/>
                <br/>
                <p style={{display: 'flex',width: '340px',margin: '0px', justifyContent: 'space-between', alignItems: 'center'}}>Уже зарегестрированы? <p style={{cursor: 'pointer', color: 'orange'}} onClick={ ()=> this.props.onOpenModal()}>Войти</p></p>
              </form>
            </div>
            {this.state.isLoaded &&
              <div className={this.state.isLoaded ? "modal_loaded active" : "modal_loaded"}>
                <div className='loader'>
                  <img src={loadIcon} alt='Loader'/>
                </div>
              </div>
            }
          </div>
        );
      }
}


export default ModalRegistration;