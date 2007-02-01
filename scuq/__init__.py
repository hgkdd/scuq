## \mainpage SCUQ - A class library for the evaluation of Scalar- or Complex-valued Uncertain Quantities.
#  This library provides classes and functions that 
#  provide support for modeling physical quantities and units. 
#  <ul>
#    <li> The Module scuq.units provides you with support for modeling and 
#         converting physical units. 
#    <li> The Module scuq.si uses the units module in order to provide you
#         with support for SI units.
#    <li> The Module scuq.arithmetic. This module contains functions
#         to assists the other modules in this libary. It also
#         contains the RationalNumber type (finished and tested).
#    <li> The module scuq.quantities allows you to join units and numeric
#         types in order to model physical quantities (finished and tested).
#    <li> The module scuq.ucomponents module models uncertain values. 
#         You can use it with the above modules in order to model uncertainty
#         in measurements. You can assign an uncertainty to
#         a numeric value and propagate it through a numpyematical
#         model. The implementation makes use of the GUM-Tree pattern.
#         This module helps you to create and use the numpyematical model
#         (finished and tested). 
#    <li> The module scuq.cucomponents can be used to evaluate the
#         uncertainty of complex-valued models in the same fashion as the
#         above module.
#  </ul>
#  \attention In contrast to the practice of explicit type checking and 
#  raising TypeErrors if an argument is invalid, we used assertions. This
#  gives you the opportunity to check your assignments in debug mode and 
#  running (relatively) fast code in release mode. The debug mode is enabled 
#  by default when invoking Python with <tt>python \<Your Code\></tt>. In
#  order to enable release mode, you should use 
#  <tt>python -O \<Your Code\></tt>.
#  \attention You should use <tt>UTF-8</tt> as default encoding. Since Greek 
#  letters represent some physical quantities, units, and dimensions, we 
#  decided to encode them in Unicode. However, you will still
#  be able to use this library if you have another default encoding. The
#  symbols will then be not printed correctly.
#  \attention In this documentation the term <tt>integer</tt> refers to
#             they Python type <tt>int</tt> as well as <tt>long</tt>. This
#             library casts all <tt>int</tt> arguments to <tt>long</tt> 
#             whenever they are used for conversions or calculations. 
#             This makes overflows unlikely, since the precision of 
#             <tt>long</tt> is limited by your systems memory in Python. 
#             That said, you will most likely encounter an 
#             <tt>MemoryError</tt>, if the accuracy of a long variable is 
#             exausted. This procedure is necessary in order to provide
#             backward compatibility to older versions of Python.
#  \note The patterns used to create the units, dimensions, and unit-operators
#        have been inspired by Java Specification Request 275 that has already 
#        been implemented in <a href="http://www.jscience.org">JScience</a> an
#        open-source library for scientific computing in Java.
#  \note The design patterns used for the evaluation of uncertainty are 
#        subject to United States patent number 7,130,761. You should 
#        arrange with the patent holders if you want to use this software 
#        within the 
#        United States of America for commercial purposes. Their patent claims
#        cover a wide variety of the field of automatic uncertainty 
#        propagation. Therefore our amendments to their proposal may also be 
#        subject to the claims of that patent. In order to stop the 
#        spread of e-patents in Europe, please support us 
#        <a href="http://www.noepatents.org/" target="_blank">here</a>.
#  \note There exists an alternative package for Python from the patent 
#        holders that allowes the automatic propagation of uncertainty.
#        Unfortunately this package does not provide any support for
#        physical quantities and units. This package does also not
#        integrate the standard numpy module and is thus less flexible than
#        our package. 
#  \author <a href="http://thomas.reidemeister.org/" target="_blank">Thomas 
#          Reidemeister</a>,
#          <a href="http://wase.urz.uni-magdeburg.de/krauthae/" 
#          target="_blank">Hans Georg Krauth&auml;user</a>
#  \see <a href="http://www.jscience.org">JScience</a>: The Java Scientific
#          Library.
#  \see <a href="http://www.jcp.org/jsr/detail/275.jsp">JSR-275</a>: Notes on 
#          the specification request. 
#  \see "The "GUM Tree": A software design pattern for handling
#       measurement uncertainty"; B. D. Hall; Industrial Research
#       Report 1291; Measurements Standards Laboratory New Zealand (2003).
#  \see "byGUM: A Python software package for calculating measurement
#        uncertainty"; B. D. Hall; Industrial Research
#        Report 1305; Measurements Standards Laboratory New Zealand (2005).
#        - Another package for calculating measurement uncertainty.
#  \see <a href="http://www.noepatents.org/" target="_blank">
#       Petition for a Software Patent Free Europe</a>. 
#       Please support us here!
#  \see <a href="http://www.uspto.gov/patft/index.html" target="_blank">
#       United States Patent and Trademark Office: Patent Database</a>. You
#       can lookup the claims of the patent, mentioned above, here.

## \file __init__.py
#  \brief This file is evaluated whenever the quantities package is loaded.
# 
#  It loads the modules neccessary for operating this package. It also
#  performs some global initialization.
#  \author <a href="http://thomas.reidemeister.org/" target="_blank">Thomas 
#          Reidemeister</a>

## \namespace scuq::__init__
#  \brief This namespace does only contain variables for global initialization.

## \namespace scuq
#  \brief The namespace containing this library.

## \page Notation Coercion Rules
# In this section, we provide a complete set of coercion rules.
# These are used to convert among our data types in order to
# preserve the semantics. Coercion is performed whenever a
# binary operation is excecuted on one of our defined types.
# The goal of the coercion rules is to provide equal data types
# for both of the arguments of a binary operation.
# For example the multiplication of a rational number and a
# floating point number should be performed by converting
# the rational number to a floating point number. Coercion is symmeric. 
# Therefore the same applies to multiplications of floating point
# with rational numbers.
# We denote the rule as follows. 
# \f[{a} \times {f} \rightarrow {f(a)} \times {f} \f]
# We begin by introducing the notation.
# <ul>
#   <li>\f${f}\f$ and \f${f(x)}\f$ refer to instances of 
#       <tt>float</tt>. The second argument is used to 
#       express the conversion of \f$x\f$ to a <tt>float</tt>.
#   <li>\f${z}\f$ and \f${z(x)}\f$ refer to instances of 
#       <tt>long</tt> and <tt>int</tt>. The second argument is used to 
#       express the conversion of \f$x\f$ to a <tt>long</tt>.
#   <li>\f${c}\f$ and \f${c(x)}\f$ refer to instances of 
#       <tt>complex</tt>. The second argument is used to 
#       express the conversion of \f$x\f$ to a <tt>complex</tt>.
#   <li>\f${nd}\f$ refers to instances of <tt>numpy.ndarray</tt>.
#   <li>\f${a}\f$ and \f${a(x)}\f$ refer to instances of 
#       arithmetic.RationalNumber. The second argument is used to 
#       express the conversion of \f$x\f$ to an instance of 
#       arithmetic.RationalNumber. The conversion is implemented in
#       arithmetic.RationalNumber.value_of.
#   <li>\f${q}\f$ and \f${q(x)}\f$ refer to instances of 
#       quantities.Quantity. The second argument is used to 
#       express the conversion of \f$x\f$ to an instance of 
#       quantities.Quantity. The conversion is implemented in
#       quantities.Quantity.value_of.
#   <li>\f${u_s}\f$ and \f${u_s(x)}\f$ refer to instances of 
#       ucomponents.UncertainComponent. The second argument is used to 
#       express the conversion of \f$x\f$ to an instance of 
#       ucomponents.UncertainComponent. The conversion is implemented in
#       ucomponents.UncertainComponent.value_of.
#   <li>\f${u_c}\f$ and \f${u_c(x)}\f$ refer to instances of 
#       cucomponents.CUncertainComponent. The second argument is used to 
#       express the conversion of \f$x\f$ to an instance of 
#       cucomponents.CUncertainComponent. The conversion is implemented in
#       cucomponents.CUncertainComponent.value_of.
#   <li>\f${u}\f$ denotes an instance of units.Unit.
#   <li>\f${\emptyset}\f$ denotes an undefined operation.
# </ul>
#
# <b>The cohercion rules by type:</b>
# <ul>
#    <li>Type: arithmetic.RationalNumber
#        \f{eqnarray}
#            a \times a & \rightarrow & a \times a \\
#            a \times z & \rightarrow & a \times a(z) \\
#            a \times c & \rightarrow & c(a) \times c \\
#            a \times f & \rightarrow & f(a) \times f \\
#            a \times q & \rightarrow & q(a) \times q \\
#            a \times u_s & \rightarrow & u_s(a) \times u_s \\
#            a \times u_c & \rightarrow & u_c(a) \times u_c \\
#            a \times u & \rightarrow & \emptyset \\
#            a \times nd & \rightarrow & \emptyset
#        \f}
#    <li>Type: quantities.Quantity
#        \f{eqnarray}
#            q \times q & \rightarrow & q \times q \\
#            q \times z & \rightarrow & q \times q(z) \\
#            q \times c & \rightarrow & q \times q(c) \\
#            q \times f & \rightarrow & q \times q(f) \\
#            q \times u_s & \rightarrow & q \times q(u_s) \\
#            q \times u_c & \rightarrow & q \times q(u_c) \\
#            q \times nd & \rightarrow & q \times q(nd) \\
#            q \times u & \rightarrow & \emptyset
#        \f}
#    <li>Type: ucomponents.UncertainComponent
#        \f{eqnarray}
#            u_s \times u_s & \rightarrow & u_s \times u_s \\
#            u_s \times z & \rightarrow & u_s \times u_s(z) \\
#            u_s \times f & \rightarrow & u_s \times u_s(f) \\
#            u_s \times nd & \rightarrow & \emptyset \\
#            u_s \times u_c & \rightarrow & \emptyset \\
#            u_s \times c & \rightarrow & \emptyset \\
#            u_s \times u & \rightarrow & \emptyset
#        \f}
#    <li>Type: cucomponents.CUncertainComponent
#        \f{eqnarray}
#            u_c \times u_c & \rightarrow & u_c \times u_c \\
#            u_c \times z & \rightarrow & u_c \times u_c(z) \\
#            u_c \times f & \rightarrow & u_c \times u_c(f) \\
#            u_c \times c & \rightarrow & u_c \times u_c(c) \\
#            u_c \times nd & \rightarrow & \emptyset \\
#            u_c \times u & \rightarrow & \emptyset
#        \f}
#
# </ul> 
# \attention The binary operators from <tt>numpy</tt>, such as 
#            numpy.arctan2, and numpy.hypot, do not implement
#            coercion. Instead, they broadcast arctan2 to the first
#            argument. Therefore our coercion rules may not be
#            symmetric when using operators from numpy.

## Modules contained within the quantities package.
__all__ = ["arithmetic", "units", "qexceptions", "si", "quantities", "operators", "ucomponents", "cucomponents"]
