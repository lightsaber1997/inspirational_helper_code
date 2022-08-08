package com.example.demo.user;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomUserDetailsDAO {
	public List<CustomUserDetails> selectUserDetailsList();
	public CustomUserDetails selectUserByLoginId(
			@Param("loginId") String loginId);
	public void insertUser(
			@Param("id") int id,
			@Param("loginId") String loginId,
			@Param("encryptedPassword") String encryptedPassword,
			@Param("email") String email,
			@Param("phoneNumber") String phoneNumber,
			@Param("authority") String authority,
			@Param("userNameInApp") String userNameInApp,
			@Param("realName") String realName);
	
}