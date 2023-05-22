import React, { PureComponent } from 'react';
import HandleBack from './HandleBack';
import Hyperview from 'hyperview';
import moment from 'moment';
import { MAIN_STACK_NAME, MODAL_STACK_NAME } from './constants';

export default class HyperviewScreen extends PureComponent {
  goBack = () => {
    this.props.navigation.pop();
  }

  closeModal = () => {
    this.props.navigation.pop();
  }

  push = (params) => {
    // If we're in a modal stack, push the next screen on the modal stack.
    // If we're in the main stack, push the next screen in the main stack.
    // Modal stacks will have modal param set.
    const modal = this.props.route.params?.modal ?? false;
    this.props.navigation.push(
      modal ? MODAL_STACK_NAME : MAIN_STACK_NAME,
      {
        modal,
        ...params,
      }
    );
  }

  navigate = (params, key) => {
    this.props.navigation.navigate({ key, params, routeName: MAIN_STACK_NAME });
  }

  openModal = (params) => {
    this.props.navigation.push(MODAL_STACK_NAME, params);
  }

  formatDate = (date, format) => moment(date).format(format);

  /** 
   * fetch function used by Hyperview screens. By default, it adds
   * header to prevent caching requests.
   */
  fetchWrapper = (input, init = { headers: {} }) => {
    return fetch(input, {
      ...init,
      mode: "cors",
      headers: {
        // TODO Don't cache requests for the demo, probably need to be changed for production
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        Expires: 0,
        Pragma: 'no-cache',
        ...init.headers,
      }
    });
  }

  render() {
    const entrypointUrl = this.props.route.params?.url;

    return (
      <HandleBack>
        <Hyperview
          back={this.goBack}
          closeModal={this.closeModal}
          entrypointUrl={entrypointUrl}
          fetch={this.fetchWrapper}
          formatDate={this.formatDate}
          navigate={this.navigate}
          navigation={this.props.navigation}
          openModal={this.openModal}
          push={this.push}
          route={this.props.route}
        />
      </HandleBack>
    );
  }
}
