# Python Hyperview

This project showcase how to build a mobile application using python web frameworks (currently only django is
implemented) and hyperview. It is meant to be
a guide / reference for poeople like me who got lost with just the hyperiew docs
This is just to hoeplly simplify the process of getting started with hyperview with a python web framework.

## Prerequisites

- Full android or ios or both development setup including a simulator (or physical device)
- python
- nodejs , npm or yarn

## What is hyperview ?

It is more appropriate to simple CRUD applications, when you need an application alongisde your web app that expose few
of the
web app feature, for more complex application you might want to look into things like flutter, react-native, ionic, etc.

Hyperview is not a python solution, you could use it with any framework, in fact you could use the hyperview_starter to
generate your own hyperview client no matter which framework you use (as long as you can install copier), and I hope
this
guide might me understable to help even if you don't use python.



## Guide

The `mobile_client` is the hyperview client and was generated using
the [hyperview_starter](https://github.com/Tobi-De/hyperview_starter)
Then there is a folder for the app for each framework implement, currently only django is implemented, fastapi is coming
soon, but if you know
enough of python you should have minimal issue to replace the same things for your framework of choice.


### How does it work ?

### HXML, the format use by hypermedia

HXML hypermedia by hypermidia systems


Summary

    HXML looks similar to HTML, but it uses elements that correspond to mobile UIs, like <screen>, <header>, <list> and more.
    HXML includes input elements that implement common patterns in mobile apps, such as <switch>, <select-single>, and <select-multiple>.
    New UI components can be added to HXML using namespaced elements. The Hyperview client can be easily extended to render these new elements.
    Interactions in HXML are defined using <behavior> elements. Inspired by htmx, <behavior> elements decouple user interactions (triggers) from the resulting actions.
    Navigation between screens in Hyperview is done using behaviors with navigation actions, like push, back, new, and close.
    Updates to screens in Hyperview are defined using behaviors with update actions, such as replace and append.
    System interactions in Hyperview are defined using behaviors with system actions, such as alert and share.
    New actions can be added to HXML using namespaced attributes. The Hyperview client can be easily extended to interpret the new actions.

Some example of what HXML look like

How to return xml response

https://github.com/bigskysoftware/contact-app

## Buiding standalone apps

https://docs.expo.dev/archive/classic-updates/building-standalone-apps/

## Setup

The application build is the the contacts app from the [hypermedia systems](https://hypermedia.systems/) book, so there
is even
some htmx showcase.

## Resources

- [hyperview_starter](https://github.com/Tobi-De/hyperview_starter)
- [Section **Bringing Hypermedia To Mobile**](https://hypermedia.systems/book/hyperview-a-mobile-hypermedia/)
  of [hypermedia systems](https://hypermedia.systems/)
- [hyperview website](https://hyperview.org/)
- [htmx docs](https://htmx.org/)
- [django docs](https://docs.djangoproject.com/)
- [django-cors-headers docs](https://github.com/adamchainz/django-cors-headers)
- [Expo](https://expo.dev/)
- [React Native](https://reactnative.dev/)

## Common issues

- If you changes something in the the mobile client code don't forget to reload your app with `r` in the expo terminal.

## Issues

If you have any issues during opening and it is purely related to the setup of the project, feel free to opened an
issues on this repository
but if it seems to be purely and hyperview issues open an issues on their repository.

## Altenative approach

### Native

- flutter
- react-native
- ionic
-

## Web view (Server driven UI)

They use the same approach as hyperview, the server driven UI patterns but don't render native components.

- apache cordova
- https://pub.dev/packages/sdui
- https://github.com/divkit/divkit

Tweet / masstodon

I'be been experimenting with building mobile app application with django and hyperview the last two days, I've put up
this repo
for anyone like me who got lost a bit after reading the hyperview docs.