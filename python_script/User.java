package com.inspirational.userDetails;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;


@Repository
public interface CustomUserDetailsDAO {
	public CustomUserDetails selectUserByLoginId(
			@Param("loginId") String loginId);
}
