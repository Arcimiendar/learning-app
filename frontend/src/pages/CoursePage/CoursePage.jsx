import PropTypes from 'prop-types'
import React from 'react'
import CourseItem from '../../components/CourseItem/CourseItem'

function CoursePage({ name, items }) {
  return (
    <div className="course">
      <span className="course__name">Курс «{name}»</span>
      {items.map(({ type, id, ...other }) => (
        <CourseItem type={type} id={id} {...other} key={`${type}-${id}`} />
      ))}
    </div>
  )
}

CoursePage.propTypes = {
  name: PropTypes.string.isRequired,
  items: PropTypes.arrayOf(
    PropTypes.shape({
      type: PropTypes.string.isRequired,
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      completed: PropTypes.bool.isRequired,
    }).isRequired
  ).isRequired,
}

export default CoursePage
