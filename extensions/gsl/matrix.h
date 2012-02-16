// -*- C++ -*-
// 
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2012 all rights reserved
// 

#if !defined(gsl_extension_matrix_h)
#define gsl_extension_matrix_h


// place everything in my private namespace
namespace gsl {
    namespace matrix {

        // allocate
        extern const char * const allocate__name__;
        extern const char * const allocate__doc__;
        PyObject * allocate(PyObject *, PyObject *);

        // set_zero
        extern const char * const zero__name__;
        extern const char * const zero__doc__;
        PyObject * zero(PyObject *, PyObject *);

        // set_all
        extern const char * const fill__name__;
        extern const char * const fill__doc__;
        PyObject * fill(PyObject *, PyObject *);

        // set_identity
        extern const char * const identity__name__;
        extern const char * const identity__doc__;
        PyObject * identity(PyObject *, PyObject *);

        // matrix_get
        extern const char * const get__name__;
        extern const char * const get__doc__;
        PyObject * get(PyObject *, PyObject *);

        // matrix_set
        extern const char * const set__name__;
        extern const char * const set__doc__;
        PyObject * set(PyObject *, PyObject *);

        // matrix_contains
        extern const char * const contains__name__;
        extern const char * const contains__doc__;
        PyObject * contains(PyObject *, PyObject *);

        // matrix_max
        extern const char * const max__name__;
        extern const char * const max__doc__;
        PyObject * max(PyObject *, PyObject *);

        // matrix_min
        extern const char * const min__name__;
        extern const char * const min__doc__;
        PyObject * min(PyObject *, PyObject *);

        // matrix_minmax
        extern const char * const minmax__name__;
        extern const char * const minmax__doc__;
        PyObject * minmax(PyObject *, PyObject *);

        // matrix_add
        extern const char * const add__name__;
        extern const char * const add__doc__;
        PyObject * add(PyObject *, PyObject *);

        // matrix_sub
        extern const char * const sub__name__;
        extern const char * const sub__doc__;
        PyObject * sub(PyObject *, PyObject *);

        // matrix_mul
        extern const char * const mul__name__;
        extern const char * const mul__doc__;
        PyObject * mul(PyObject *, PyObject *);

        // matrix_div
        extern const char * const div__name__;
        extern const char * const div__doc__;
        PyObject * div(PyObject *, PyObject *);

        // matrix_add_constant
        extern const char * const shift__name__;
        extern const char * const shift__doc__;
        PyObject * shift(PyObject *, PyObject *);

        // matrix_scale
        extern const char * const scale__name__;
        extern const char * const scale__doc__;
        PyObject * scale(PyObject *, PyObject *);

    } // of namespace matrix
} // of namespace gsl

#endif

// end of file