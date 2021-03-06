add_subdirectory(libpyre)

set(testfiles
journal/colors.py
journal/crosstalk.py
journal/debug-activation.py
journal/debug-injection.py
journal/debug.py
journal/error-activation.py
journal/error-injection.py
journal/error.py
journal/firewall-activation.py
journal/firewall-injection.py
journal/firewall.py
journal/info-activation.py
journal/info-injection.py
journal/info.py
journal/sanity.py
journal/warning-activation.py
journal/warning-injection.py
journal/warning.py
merlin/components/merlin_curator.py
merlin/components/merlin_packages.py
merlin/components/merlin_shell.py
merlin/components/merlin_spell.py
merlin/components/sanity.py
pyre/algebraic/arithmetic.py
pyre/algebraic/boolean.py
pyre/algebraic/dependencies.py
pyre/algebraic/exceptions.py
pyre/algebraic/layout.py
pyre/algebraic/ordering.py
pyre/algebraic/patch.py
pyre/algebraic/sanity.py
pyre/calc/aggregators.py
pyre/calc/algebra.py
pyre/calc/containers.py
pyre/calc/exceptions.py
pyre/calc/explicit.py
pyre/calc/expression.py
pyre/calc/expression_circular.py
pyre/calc/expression_escaped.py
pyre/calc/expression_resolution.py
pyre/calc/expression_syntaxerror.py
pyre/calc/expression_typeerror.py
pyre/calc/hierarchical.py
pyre/calc/hierarchical_alias.py
pyre/calc/hierarchical_contains.py
pyre/calc/hierarchical_group.py
pyre/calc/hierarchical_patch.py
pyre/calc/interpolation.py
pyre/calc/interpolation_circular.py
pyre/calc/interpolation_escaped.py
pyre/calc/memo.py
pyre/calc/memo_expression.py
pyre/calc/memo_interpolation.py
pyre/calc/memo_model.py
pyre/calc/model.py
pyre/calc/node.py
pyre/calc/node_class.py
pyre/calc/node_instance.py
pyre/calc/operations.py
pyre/calc/patch.py
pyre/calc/probe.py
pyre/calc/reductors.py
pyre/calc/reference.py
pyre/calc/replace.py
pyre/calc/replace_probe.py
pyre/calc/sanity.py
pyre/calc/substitute.py
pyre/calc/sum.py
pyre/codecs/cfg.py
pyre/codecs/cfg_badToken.py
pyre/codecs/cfg_close.py
pyre/codecs/cfg_empty.py
pyre/codecs/cfg_marker.py
pyre/codecs/cfg_open.py
pyre/codecs/exceptions.py
pyre/codecs/manager.py
pyre/codecs/pfg.py
pyre/codecs/pfg_componentConditional.py
pyre/codecs/pfg_componentConditionalNested.py
pyre/codecs/pfg_componentFamily.py
pyre/codecs/pfg_componentName.py
pyre/codecs/pfg_empty.py
pyre/codecs/pfg_package.py
pyre/codecs/pfg_packageNested.py
pyre/codecs/pfg_sample.py
pyre/codecs/pml.py
pyre/codecs/pml_badAttribute.py
pyre/codecs/pml_badNode.py
pyre/codecs/pml_badRoot.py
pyre/codecs/pml_componentConditional.py
pyre/codecs/pml_componentConditionalNested.py
pyre/codecs/pml_componentFamily.py
pyre/codecs/pml_componentName.py
pyre/codecs/pml_empty.py
pyre/codecs/pml_package.py
pyre/codecs/pml_packageNested.py
pyre/codecs/pml_sample.py
pyre/codecs/pml_unknownNode.py
pyre/codecs/sanity.py
pyre/components/actor.py
pyre/components/component.py
pyre/components/component_aliases.py
pyre/components/component_bad_implementations.py
pyre/components/component_behavior.py
pyre/components/component_class_binding.py
pyre/components/component_class_binding_conversions.py
pyre/components/component_class_binding_import.py
pyre/components/component_class_binding_vfs.py
pyre/components/component_class_configuration.py
pyre/components/component_class_configuration_inheritance.py
pyre/components/component_class_configuration_inheritance_multi.py
pyre/components/component_class_inventory.py
pyre/components/component_class_private_locators.py
pyre/components/component_class_public_locators.py
pyre/components/component_class_registration.py
pyre/components/component_class_registration_inventory.py
pyre/components/component_class_registration_model.py
pyre/components/component_class_trait_matrix.py
pyre/components/component_class_validation.py
pyre/components/component_compatibility.py
pyre/components/component_compatibility_reports.py
pyre/components/component_defaults.py
pyre/components/component_dict.py
pyre/components/component_facility.py
pyre/components/component_family.py
pyre/components/component_implements.py
pyre/components/component_inheritance.py
pyre/components/component_inheritance_multi.py
pyre/components/component_instance_binding.py
pyre/components/component_instance_binding_configuration.py
pyre/components/component_instance_binding_deferred.py
pyre/components/component_instance_binding_existing.py
pyre/components/component_instance_binding_implicit.py
pyre/components/component_instance_configuration.py
pyre/components/component_instance_configuration_constructor.py
pyre/components/component_instance_configuration_inheritance.py
pyre/components/component_instance_configuration_inheritance_multi.py
pyre/components/component_instance_private_locators.py
pyre/components/component_instance_public_locators.py
pyre/components/component_instance_registration.py
pyre/components/component_instance_validation.py
pyre/components/component_instantiation.py
pyre/components/component_invocation.py
pyre/components/component_list.py
pyre/components/component_property.py
pyre/components/component_shadow.py
pyre/components/component_slots.py
pyre/components/exceptions.py
pyre/components/monitor.py
pyre/components/protocol.py
pyre/components/protocol_behavior.py
pyre/components/protocol_compatibility.py
pyre/components/protocol_compatibility_reports.py
pyre/components/protocol_family.py
pyre/components/protocol_inheritance.py
pyre/components/protocol_inheritance_multi.py
pyre/components/protocol_instantiation.py
pyre/components/protocol_property.py
pyre/components/protocol_shadow.py
pyre/components/quad.py
pyre/components/requirement.py
pyre/components/role.py
pyre/components/sample.py
pyre/components/sanity.py
pyre/components/tracker.py
pyre/config/command.py
pyre/config/command_argv.py
pyre/config/command_config.py
pyre/config/configurator.py
pyre/config/configurator_assignments.py
pyre/config/configurator_load_cfg.py
pyre/config/configurator_load_pfg.py
pyre/config/configurator_load_pml.py
pyre/config/configurator_locators.py
pyre/config/events.py
pyre/config/events_assignments.py
pyre/config/exceptions.py
pyre/config/sanity.py
pyre/constraints/and.py
pyre/constraints/exceptions.py
pyre/constraints/isAll.py
pyre/constraints/isAny.py
pyre/constraints/isBetween.py
pyre/constraints/isEqual.py
pyre/constraints/isGreater.py
pyre/constraints/isGreaterEqual.py
pyre/constraints/isLess.py
pyre/constraints/isLessEqual.py
pyre/constraints/isLike.py
pyre/constraints/isMember.py
pyre/constraints/isNegative.py
pyre/constraints/isNot.py
pyre/constraints/isPositive.py
pyre/constraints/isSubset.py
pyre/constraints/or.py
pyre/constraints/sanity.py
pyre/db/persistent_declaration.py
pyre/db/query_collation.py
pyre/db/query_collation_explicit.py
pyre/db/query_collation_expression.py
pyre/db/query_inheritance.py
pyre/db/query_projection.py
pyre/db/query_projection_expressions.py
pyre/db/query_projection_multitable.py
pyre/db/query_restriction.py
pyre/db/query_star.py
pyre/db/sanity.py
pyre/db/table_annotations.py
pyre/db/table_create.py
pyre/db/table_declaration.py
pyre/db/table_delete.py
pyre/db/table_inheritance.py
pyre/db/table_insert.py
pyre/db/table_instantiation.py
pyre/db/table_references.py
pyre/db/table_update.py
pyre/descriptors/arrays.py
pyre/descriptors/booleans.py
pyre/descriptors/converters.py
pyre/descriptors/dates.py
pyre/descriptors/decimals.py
pyre/descriptors/defaults.py
pyre/descriptors/dimensionals.py
pyre/descriptors/filtering.py
pyre/descriptors/floats.py
pyre/descriptors/harvesting.py
pyre/descriptors/inets.py
pyre/descriptors/inheritance.py
pyre/descriptors/integers.py
pyre/descriptors/istreams.py
pyre/descriptors/lists.py
pyre/descriptors/ostreams.py
pyre/descriptors/paths.py
pyre/descriptors/sanity.py
pyre/descriptors/sets.py
pyre/descriptors/strings.py
pyre/descriptors/times.py
pyre/descriptors/timestamps.py
pyre/descriptors/tuples.py
pyre/descriptors/uris.py
pyre/externals/blas.py
pyre/externals/cython.py
pyre/externals/gcc.py
pyre/externals/gsl.py
pyre/externals/hdf5.py
pyre/externals/locate.py
pyre/externals/mpi.py
pyre/externals/postgres.py
pyre/externals/python.py
pyre/externals/sanity.py
pyre/externals/vtk.py
pyre/filesystem/directory_walker.py
pyre/filesystem/exceptions.py
pyre/filesystem/filesystem.py
pyre/filesystem/finder.py
pyre/filesystem/finder_pattern.py
pyre/filesystem/folder.py
pyre/filesystem/local.py
pyre/filesystem/local_find.py
pyre/filesystem/local_leaks.py
pyre/filesystem/local_make.py
pyre/filesystem/local_open.py
pyre/filesystem/local_rootNonexistent.py
pyre/filesystem/local_rootNotDirectory.py
pyre/filesystem/node.py
pyre/filesystem/sanity.py
pyre/filesystem/simple_explorer.py
pyre/filesystem/stat_recognizer.py
pyre/filesystem/tree_explorer.py
pyre/filesystem/virtual.py
pyre/filesystem/virtual_access.py
pyre/filesystem/virtual_find.py
pyre/filesystem/virtual_info.py
pyre/filesystem/virtual_insert.py
pyre/filesystem/virtual_insert_badNode.py
pyre/filesystem/virtual_insert_multiple.py
pyre/filesystem/virtual_leaks.py
pyre/filesystem/virtual_subscripts.py
pyre/filesystem/zip_open.py
pyre/filesystem/zip_rootNonexistent.py
pyre/filesystem/zip_rootNotZipfile.py
pyre/filesystem/zip.py
pyre/flow/sanity.py
pyre/framework/exceptions.py
pyre/framework/executive.py
pyre/framework/executive_configuration.py
pyre/framework/executive_resolve.py
pyre/framework/executive_resolve_badImport.py
pyre/framework/executive_resolve_duplicate.py
pyre/framework/executive_resolve_syntaxError.py
pyre/framework/executive_shelves.py
pyre/framework/externals.py
pyre/framework/fileserver.py
pyre/framework/fileserver_mount.py
pyre/framework/fileserver_uri.py
pyre/framework/linker.py
pyre/framework/linker_codecs.py
pyre/framework/linker_shelves.py
pyre/framework/nameserver.py
pyre/framework/nameserver_access.py
pyre/framework/nameserver_aliases.py
pyre/framework/registrar.py
pyre/framework/sample.py
pyre/framework/sanity.py
pyre/framework/slot.py
pyre/framework/slot_algebra.py
pyre/framework/slot_instance.py
pyre/framework/slot_update.py
pyre/grid/grid.py
pyre/grid/sanity.py
pyre/grid/tile.py
pyre/ipc/pickler.py
pyre/ipc/pickler_over_pipe.py
pyre/ipc/pickler_over_tcp.py
pyre/ipc/pipe.py
pyre/ipc/sanity.py
pyre/ipc/scheduler.py
pyre/ipc/scheduler_alarms.py
pyre/ipc/scheduler_instantiation.py
pyre/ipc/selector.py
pyre/ipc/selector_alarms.py
pyre/ipc/selector_instantiation.py
pyre/ipc/selector_pickler_over_pipe.py
pyre/ipc/selector_pickler_over_tcp.py
pyre/ipc/selector_signals.py
pyre/ipc/tcp.py
pyre/nexus/node.py
pyre/nexus/node_instantiation.py
pyre/nexus/node_signals.py
pyre/nexus/pool.py
pyre/nexus/sanity.py
pyre/parsing/exceptions.py
pyre/parsing/lexing.py
pyre/parsing/lexing_tokenizationError.py
pyre/parsing/sanity.py
pyre/parsing/scanner.py
pyre/patterns/classifier.py
pyre/patterns/extent.py
pyre/patterns/named.py
pyre/patterns/observable.py
pyre/patterns/pathhash.py
pyre/patterns/powerset.py
pyre/patterns/sanity.py
pyre/patterns/singleton.py
pyre/platforms/host.py
pyre/platforms/sanity.py
pyre/primitives/path.py
pyre/primitives/path_arithmetic.py
pyre/primitives/path_parts.py
pyre/primitives/path_resolution.py
pyre/primitives/path_tuple.py
pyre/primitives/sanity.py
pyre/pyre/defaults.py
pyre/pyre/loadConfiguration.py
pyre/pyre/play.py
pyre/pyre/resolve.py
pyre/pyre/sample.py
pyre/pyre/sanity.py
pyre/pyre/spaces.py
pyre/records/complex_immutable_conversions.py
pyre/records/complex_immutable_data.py
pyre/records/complex_immutable_kwds.py
pyre/records/complex_immutable_validations.py
pyre/records/complex_inheritance.py
pyre/records/complex_inheritance_multi.py
pyre/records/complex_layout.py
pyre/records/complex_mutable_conversions.py
pyre/records/complex_mutable_data.py
pyre/records/complex_mutable_kwds.py
pyre/records/complex_mutable_validations.py
pyre/records/csv_bad_source.py
pyre/records/csv_instance.py
pyre/records/csv_read_complex.py
pyre/records/csv_read_mutable.py
pyre/records/csv_read_partial.py
pyre/records/csv_read_simple.py
pyre/records/sanity.py
pyre/records/simple.py
pyre/records/simple_immutable_conversions.py
pyre/records/simple_immutable_data.py
pyre/records/simple_immutable_kwds.py
pyre/records/simple_immutable_validations.py
pyre/records/simple_inheritance.py
pyre/records/simple_inheritance_multi.py
pyre/records/simple_layout.py
pyre/records/simple_mutable_conversions.py
pyre/records/simple_mutable_data.py
pyre/records/simple_mutable_kwds.py
pyre/records/simple_mutable_validations.py
pyre/schemata/arrays.py
pyre/schemata/booleans.py
pyre/schemata/catalogs.py
pyre/schemata/dates.py
pyre/schemata/decimals.py
pyre/schemata/dimensionals.py
pyre/schemata/exceptions.py
pyre/schemata/floats.py
pyre/schemata/fractional.py
pyre/schemata/inets.py
pyre/schemata/integers.py
pyre/schemata/istreams.py
pyre/schemata/lists.py
pyre/schemata/mappings.py
pyre/schemata/ostreams.py
pyre/schemata/paths.py
pyre/schemata/sanity.py
pyre/schemata/sets.py
pyre/schemata/strings.py
pyre/schemata/times.py
pyre/schemata/timestamps.py
pyre/schemata/tuples.py
pyre/schemata/typed.py
pyre/schemata/uris.py
pyre/shells/application_inheritance.py
pyre/shells/application_instantiation.py
pyre/shells/application_namespace.py
pyre/shells/application_sanity.py
pyre/shells/colors24bit.py
pyre/shells/colors256.py
pyre/shells/daemon_instantiation.py
pyre/shells/daemon_launching.py
pyre/shells/daemon_sanity.py
pyre/shells/fork_instantiation.py
pyre/shells/fork_launching.py
pyre/shells/fork_sanity.py
pyre/shells/sanity.py
pyre/shells/script_instantiation.py
pyre/shells/script_launching.py
pyre/shells/script_sanity.py
pyre/tabular/chart.py
pyre/tabular/chart_class_inheritance.py
pyre/tabular/chart_class_layout.py
pyre/tabular/chart_filter.py
pyre/tabular/chart_inferred.py
pyre/tabular/chart_instance.py
pyre/tabular/chart_interval.py
pyre/tabular/chart_interval_config.py
pyre/tabular/chart_sales.py
pyre/tabular/csv_instance.py
pyre/tabular/csv_read.py
pyre/tabular/pivot.py
pyre/tabular/sanity.py
pyre/tabular/sheet.py
pyre/tabular/sheet_class_inheritance.py
pyre/tabular/sheet_class_inheritance_multi.py
pyre/tabular/sheet_class_inheritance_record.py
pyre/tabular/sheet_class_layout.py
pyre/tabular/sheet_class_record.py
pyre/tabular/sheet_columns.py
pyre/tabular/sheet_index.py
pyre/tabular/sheet_instance.py
pyre/tabular/sheet_populate.py
pyre/tabular/sheet_updates.py
pyre/tabular/view.py
pyre/timers/native_timer.py
pyre/timers/pyre_timer.py
pyre/timers/python_timer.py
pyre/timers/python_timer_errors.py
pyre/timers/sanity.py
pyre/tracking/chain.py
pyre/tracking/command.py
pyre/tracking/file.py
pyre/tracking/fileregion.py
pyre/tracking/lookup.py
pyre/tracking/sanity.py
pyre/tracking/script.py
pyre/tracking/simple.py
pyre/units/algebra.py
pyre/units/exceptions.py
pyre/units/formatting.py
pyre/units/one.py
pyre/units/parser.py
pyre/units/sanity.py
pyre/weaver/document_c.py
pyre/weaver/document_csh.py
pyre/weaver/document_cxx.py
pyre/weaver/document_f77.py
pyre/weaver/document_f90.py
pyre/weaver/document_html.py
pyre/weaver/document_latex.py
pyre/weaver/document_make.py
pyre/weaver/document_perl.py
pyre/weaver/document_pfg.py
pyre/weaver/document_python.py
pyre/weaver/document_sh.py
pyre/weaver/document_sql.py
pyre/weaver/document_svg.py
pyre/weaver/document_tex.py
pyre/weaver/document_xml.py
pyre/weaver/expressions_c.py
pyre/weaver/expressions_cxx.py
pyre/weaver/expressions_python.py
pyre/weaver/expressions_sql.py
pyre/weaver/sanity.py
pyre/weaver/weaver_raw.py
pyre/xml/blank.py
pyre/xml/document.py
pyre/xml/empty.py
pyre/xml/exceptions.py
pyre/xml/fs.py
pyre/xml/fs_extra.py
pyre/xml/fs_namespaces.py
pyre/xml/fs_schema.py
pyre/xml/namespaces.py
pyre/xml/reader.py
pyre/xml/sanity.py
pyre/xml/schema.py
python/algebra.py
python/argv.py
python/arithmetic.py
python/classattr.py
python/decorators.py
python/descriptors.py
python/dict_in.py
python/dict_update.py
python/execv.py
python/expressions.py
python/files.py
python/format.py
python/functions.py
python/inheritance_multiple.py
python/inheritance_properties.py
python/inheritance_shadow.py
python/initialization.py
python/locale_codec.py
python/locale_open.py
python/metaclass.py
python/metaclass_callsequence.py
python/metaclass_dict.py
python/metaclass_dynamic.py
python/metaclass_inheritance.py
python/metaclass_interface.py
python/metaclass_kwds.py
python/metaclass_prime.py
python/metaclass_refcount.py
python/moditer.py
python/slots.py
sqlite/sanity.py
sqlite/sqlite_attach.py
sqlite/sqlite_database.py
sqlite/sqlite_references.py
sqlite/sqlite_table.py
)

if(WITH_CUDA)
    list(APPEND testfiles
        cuda/extension.py
        cuda/manager.py
        cuda/sanity.py
        )
endif()

if(GSL_FOUND)
    list(APPEND testfiles
        gsl/blas.py
        gsl/blas_dasum.py
        gsl/blas_daxpy.py
        gsl/blas_ddot.py
        gsl/blas_dgemm.py
        gsl/blas_dgemv.py
        gsl/blas_dnrm2.py
        gsl/blas_dsymm.py
        gsl/blas_dsymv.py
        gsl/blas_dtrmm.py
        gsl/blas_dtrmv.py
        gsl/blas_dtrsv.py
        gsl/linalg.py
        gsl/linalg_LU.py
        gsl/matrix.py
        gsl/matrix_add.py
        gsl/matrix_allocate.py
        gsl/matrix_bcast.py
        gsl/matrix_clone.py
        gsl/matrix_collect.py
        gsl/matrix_contains.py
        gsl/matrix_div.py
        gsl/matrix_fill.py
        gsl/matrix_max.py
        gsl/matrix_min.py
        gsl/matrix_minmax.py
        gsl/matrix_mul.py
        gsl/matrix_partition.py
        gsl/matrix_print.py
        gsl/matrix_random.py
        gsl/matrix_scale.py
        gsl/matrix_set.py
        gsl/matrix_shift.py
        gsl/matrix_slices.py
        gsl/matrix_sub.py
        gsl/matrix_tuple.py
        gsl/matrix_view.py
        gsl/matrix_zero.py
        gsl/pdf.py
        gsl/pdf_dirichlet.py
        gsl/pdf_gaussian.py
        gsl/pdf_uniform.py
        gsl/pdf_uniform_pos.py
        gsl/permutation.py
        gsl/permutation_allocate.py
        gsl/permutation_copy.py
        gsl/permutation_get.py
        gsl/rng.py
        gsl/rng_allocate.py
        gsl/rng_available.py
        gsl/rng_float.py
        gsl/rng_int.py
        gsl/rng_range.py
        gsl/sanity.py
        gsl/stats_correlation.py
        gsl/stats_covariance.py
        gsl/vector.py
        gsl/vector_add.py
        gsl/vector_allocate.py
        gsl/vector_bcast.py
        gsl/vector_clone.py
        gsl/vector_collect.py
        gsl/vector_contains.py
        gsl/vector_div.py
        gsl/vector_fill.py
        gsl/vector_max.py
        gsl/vector_min.py
        gsl/vector_minmax.py
        gsl/vector_mul.py
        gsl/vector_partition.py
        gsl/vector_print.py
        gsl/vector_random.py
        gsl/vector_scale.py
        gsl/vector_set.py
        gsl/vector_shift.py
        gsl/vector_slices.py
        gsl/vector_sub.py
        gsl/vector_tuple.py
        gsl/vector_view.py
        gsl/vector_zero.py
        )
endif()

if(MPI_FOUND)
    list(APPEND testfiles
        mpi/bcast.py
        mpi/extension.py
        mpi/group.py
        mpi/group_exclude.py
        mpi/group_include.py
        mpi/group_setops.py
        mpi/ip.py
        mpi/max.py
        mpi/min.py
        mpi/mpirun.py
        mpi/port.py
        mpi/product.py
        mpi/restrict.py
        mpi/sanity.py
        mpi/slurm.py
        mpi/sum.py
        mpi/world.py
        )
endif()

if(PostgreSQL_FOUND)
    list(APPEND testfiles
        postgres/postgres_attach.py
        postgres/postgres_database.py
        postgres/postgres_database_create.py
        postgres/postgres_database_drop.py
        postgres/postgres_references.py
        postgres/postgres_reserved.py
        postgres/postgres_table.py
        postgres/pyrepg_connect.py
        postgres/pyrepg_exceptions.py
        postgres/pyrepg_execute.py
        postgres/pyrepg_execute_badCommand.py
        postgres/pyrepg_submit.py
        postgres/sanity.py
        postgres/sanity_pyrepg.py
        )
endif()

foreach(testfile ${testfiles})
    # generate target and test names from file/directory
    get_filename_component(fullname ${testfile} NAME)
    get_filename_component(name ${testfile} NAME_WE)
    get_filename_component(dir  ${testfile} DIRECTORY)
    string(REPLACE "/" "." testname ${dir}.${name})

    add_test(NAME ${testname}
        COMMAND ${Python3_EXECUTABLE} ./${fullname})
    set_property(TEST ${testname} PROPERTY ENVIRONMENT
        LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib
        PYTHONPATH=${CMAKE_INSTALL_PREFIX}/${PYRE_DEST_PACKAGES}
        )
    set_property(TEST ${testname} PROPERTY WORKING_DIRECTORY
        ${CMAKE_CURRENT_LIST_DIR}/${dir}
        )
endforeach()
