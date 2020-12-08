# OOP-Design-Challenge
<i>Make School CS 1.1: Final Project</i>

This project uses Python 3.7.4.

This project is an Object-Oriented Programming approach to designing a version of the Monopoly board game that can be played in the Command Line or Terminal. The rules of the classic version of Monopoly can be found here: https://www.hasbro.com/common/instruct/monins.pdf. This project cannot run actual gameplay yet, but the code in this project contains the design for the various elements of the game. 

Two main classes are `Player` and `Bank`, both of which inherit from the abstract class `Actor`. The `Actor` class contains attributes and methods that the players and the bank share: the attributes include houses, hotels, and balance, and the methods include `collect()`, `pay()`, and `sell_building()`. The `sell_building()` method is the only abstract method, since the other methods can be directly inherited by `Player` and `Bank`.


